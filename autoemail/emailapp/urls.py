
from django.contrib import admin
from django.urls import  include, path

from emailapp.views import homepage

urlpatterns = [
    path('', homepage, name='homepage')
]
