from django import forms
from .models import DescripcionMensaje
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MensajesForm(forms.ModelForm):
    class Meta:
        model=DescripcionMensaje
        fields=["textoMensaje", "destinatario"]

class RegistroForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1', 'password2']