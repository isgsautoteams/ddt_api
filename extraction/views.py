import mimetypes
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect
from .form import UploadFileForm
from .function import handle_uploaded_file
from .extraction import extract_text

ALLOWED_MIME_TYPES = [
    'application/pdf',
    'image/jpeg',
    'image/png',
    'image/gif',
]

def handle_uploaded_file(file):
    # Check if the file is a PDF
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise ValueError("Please upload file in the form of images or pdf")
    if file.size > 10000000:
        raise ValueError("You cannot upload file more than 10MB")
    # Continue with the file processing
    filename = f'{file.name}.pdf'
    with open(filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    
    return filename

def index(request):
    if request.method == 'POST':
      form = UploadFileForm(request.POST, request.FILES)
      if form.is_valid():
        try:
            filename = handle_uploaded_file(request.FILES['file'])
            extract_result = extract_text(filename)
            return HttpResponse(extract_result)
        except ValueError as e:
            return HttpResponseBadRequest(f'Error while making the API request: {e}')
      else:
          return HttpResponseBadRequest(f'There is an error while making the API request : {form.errors}')

    else:
      return HttpResponseNotAllowed(['GET'], 'For this API to work, use the POST method')

