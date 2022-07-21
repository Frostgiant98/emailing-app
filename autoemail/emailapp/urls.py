
from django import urls
from django.contrib import admin
from django.urls import  include, path
from emailapp.views import MailView

from emailapp.views import homepage
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('mail', MailView)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('api/', include(routers.urls))
]
