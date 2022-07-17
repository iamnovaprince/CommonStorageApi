
from django.contrib import admin
from django.urls import path

from .views import AWS,Azure,GCloud

urlpatterns = [
    path('aws/', AWS),
    path('azure/', Azure),
    path('gs/', GCloud),
]