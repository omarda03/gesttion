from django import forms
from .models import Deplacement

class DeplacementForm(forms.ModelForm):
    class Meta:
        model = Deplacement
        fields = ['chantier_depart', 'materiel', 'description', 'quantite', 'chantier_destination']
