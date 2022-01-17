from django.urls import path
from django.contrib import admin

from .views import *

urlpatterns = [
    path('', index),
    path('test/',ContactFormView.as_view(),  name ='add_page'),
    ]
