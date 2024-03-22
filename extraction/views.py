from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import UploadFileForm
from .function import handle_uploaded_file
from .extraction import extract_text
 
# Create your views here.
def index(request):
    if request.method == 'POST':
      form = UploadFileForm(request.POST, request.FILES)
      if form.is_valid():
        filename = handle_uploaded_file(request.FILES['file'])
        extract_result = extract_text(filename)
        return HttpResponse(extract_result)
      else:
        return HttpResponse(f'{form.errors}')
         
    else:
      return HttpResponse('Hello From OCR')