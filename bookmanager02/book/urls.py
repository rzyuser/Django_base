from django.urls import path
from book.models import index

urlpatterns = [
    path('index/',index),
]