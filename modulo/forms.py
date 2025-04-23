from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto_perfil']

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']