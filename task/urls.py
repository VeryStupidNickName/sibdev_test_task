from django.urls import path

from .views import *

urlpatterns = [
    path('task/', task, name='task'),
    path('', index_page),
]
