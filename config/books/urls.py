from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', booksListView.as_view(), name='books'),
]
