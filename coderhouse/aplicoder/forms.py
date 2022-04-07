from email.policy import default
from enum import auto
from django import forms
class Dato(forms.Form):
    nombre = forms.CharField()
    dni = forms.IntegerField()