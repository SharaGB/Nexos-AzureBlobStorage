import uuid
from io import BytesIO
from pathlib import Path

from azure.storage.blob import BlobServiceClient
from django.http import Http404

import os
from dotenv import load_dotenv

load_dotenv()
AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')
AZURE_CONTAINER_NAME = os.getenv('AZURE_CONTAINER_NAME')


def create_blob_client(filename):
    """
    Creates the blob client.
    """
    blob_service_client = BlobServiceClient.from_connection_string(
        AZURE_CONNECTION_STRING)
    container_name = AZURE_CONTAINER_NAME
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=filename)

    return blob_client


def upload_file_to_blob(file):
    """
    Uploads the given file to the blob storage.
    """
    filename = file.name
    prefix = uuid.uuid4().hex
    ext = Path(filename).suffix
    blob_name = f'{prefix}{ext}'
    file_io = BytesIO(file.read())
    blob_client = create_blob_client(blob_name)
    blob_client.upload_blob(data=file_io)

    return blob_client


def download_file_from_blob(file):
    """
    Downloads the given file from the blob storage.
    """
    blob_cliente = create_blob_client(file)
    if not blob_cliente.exists():
        raise Http404('File does not exist')
    blob_file = blob_cliente.download_blob()
    return blob_file
