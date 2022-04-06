from unicodedata import name
from django.urls import path
from aplicoder.views import *

urlpatterns = [
    path('',inicio),
    path('familiares/',family),
]
