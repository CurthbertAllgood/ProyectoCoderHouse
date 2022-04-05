from django import forms
class Dato(forms.Form):
    nombre = forms.CharField(max_length=40)
    dni = forms.IntegerField()