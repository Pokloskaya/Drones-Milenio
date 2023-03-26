# A Django view is a Python function that takes an HTTP request object as its first parameter and returns an HTTP response object. 
# The view function can retrieve data from the database, process it, and pass it to the template to be rendered as HTML or JSON. 
# It can also perform various tasks, such as authentication, authorization, and validation.

from django.shortcuts import render, redirect

#Create your views here.
def home(request):
    return render(request, 'home.html')