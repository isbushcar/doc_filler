import os
import uuid

from celery import current_app
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.views import View

from doc_filler.apps.docs_processor.forms import FileUploadForm
from doc_filler.apps.docs_processor.tasks import fill_document
from django.shortcuts import reverse


class HomeView(View):
    form = FileUploadForm

    def get(self, request):
        return render(request, 'doc_processor/home.html', {'form': self.form()})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():

            doc_path = os.path.join(settings.DOCS_DIR, str(uuid.uuid4()))
            with open(doc_path, 'wb+') as file_to_write:
                for chunk in request.FILES['doc_file']:
                    file_to_write.write(chunk)

            table_path = os.path.join(settings.DOCS_DIR, str(uuid.uuid4()))
            with open(table_path, 'wb+') as file_to_write:
                for chunk in request.FILES['table_file']:
                    file_to_write.write(chunk)

            task = fill_document.delay(doc_path, table_path)
            return redirect('task', task_id=task.id)

        return HttpResponse("Something went wrong.")


class TaskView(View):

    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        if task.status == 'SUCCESS':
            return render(
                request,
                'doc_processor/task_succeed.html',
                {'file_link': reverse('get_file', args=[task.get()])},
            )
        if task.status == 'FAILURE':
            return render(request, 'doc_processor/task_failed.html')
        if task.status == 'PENDING':
            return render(request, 'doc_processor/task_pending.html')


class GetFile(View):

    def get(self, _, file_name):
        return FileResponse(
            open(
                os.path.join(settings.DOCS_DIR, file_name),
                'rb',
            )
        )
