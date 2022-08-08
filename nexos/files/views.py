from django.shortcuts import render
from pathlib import Path
from django.contrib import messages

from .files_csv import read_csv
from .azure_controller import upload_file_to_blob


def upload_file(request):
    """ Uploads the given file to the blob storage. """
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        read_csv(file)
        filename = file.name
        ext = Path(filename).suffix
        obj = upload_file_to_blob(file)
        obj.filename = filename
        obj.ext = ext
        messages.success(request, f'Archivo {filename} subido correctamente')
        return render(request, 'files/index.html', {})
    return render(request, 'files/index.html', {})
