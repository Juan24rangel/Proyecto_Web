from django import forms
from .models import Perfil

class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto_perfil']