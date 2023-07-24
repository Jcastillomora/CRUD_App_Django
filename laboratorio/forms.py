from django import forms
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']
