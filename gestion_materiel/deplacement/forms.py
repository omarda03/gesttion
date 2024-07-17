from django import forms
from .models import Deplacement

class DeplacementForm(forms.ModelForm):
    class Meta:
        model = Deplacement
        fields = ['materiel', 'chantier_depart', 'chantier_destination', 'quantite', 'description']
