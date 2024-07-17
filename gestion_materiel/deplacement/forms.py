from django import forms
from .models import Deplacement

class DeplacementForm(forms.ModelForm):
    class Meta:
        model = Deplacement
        fields = ['chantier_depart', 'materiel', 'description', 'quantite', 'chantier_destination']

    def clean_quantite(self):
        quantite = self.cleaned_data.get('quantite')
        if quantite is None or quantite <= 0:
            raise forms.ValidationError("La quantité doit être un nombre positif.")
        return quantite
