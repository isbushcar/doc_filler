from django import forms


class FileUploadForm(forms.Form):
    doc_file = forms.FileField(required=True, label='Текстовый файл (.docx)')
    table_file = forms.FileField(required=True, label='Таблица (.xlsx)')
