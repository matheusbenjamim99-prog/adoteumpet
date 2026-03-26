from django import forms
from .models import Cachorro

class CachorroForm(forms.ModelForm):
    class Meta:
        model = Cachorro
        fields = ['nome', 'especie', 'idade', 'foto', 'descricao', 'meta', 'porte']