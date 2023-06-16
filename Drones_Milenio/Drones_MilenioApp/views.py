# A Django view is a Python function that takes an HTTP request object as its first parameter and returns an HTTP response object. 
# The view function can retrieve data from the database, process it, and pass it to the template to be rendered as HTML or JSON. 
# It can also perform various tasks, such as authentication, authorization, and validation.

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound

def react_app(request): #TENGO QUE MIRAR QUE PASA SIN EL try EXCEPT, REVISAR AL LLEGAR
    try:
        with open(settings.BASE_DIR / 'frontend/build/index.html') as file:
            return HttpResponse(file.read())
    except FileNotFoundError:
        return HttpResponseNotFound("The React app build files were not found.")

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def test(request):
    return render(request, 'test.html')