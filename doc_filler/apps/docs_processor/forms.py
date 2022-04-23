from django import forms


class FileUploadForm(forms.Form):
    doc_file = forms.FileField(required=True)
    table_file = forms.FileField(required=True)
