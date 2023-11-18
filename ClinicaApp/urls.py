from django.contrib import admin
from django.urls import path
from ClinicaApp import views

urlpatterns = [
    path('primera/' ,views.inicio),
]
