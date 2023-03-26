from django.urls import path
from django.contrib import admin
# from webApp import views as dronesViews 
#import views as dronesViews 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
]