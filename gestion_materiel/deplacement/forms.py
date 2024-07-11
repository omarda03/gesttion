from django import forms
from .models import Deplacement, Materiel

class DeplacementForm(forms.ModelForm):
    class Meta:
        model = Deplacement
        fields = ['materiel', 'chantier_depart', 'chantier_destination', 'quantite']

    def clean(self):
        cleaned_data = super().clean()
        materiel = cleaned_data.get('materiel')
        chantier_depart = cleaned_data.get('chantier_depart')
        quantite = cleaned_data.get('quantite')

        if not materiel or not chantier_depart or not quantite:
            raise forms.ValidationError("Veuillez remplir tous les champs.")

        # Vérifiez si le matériel est présent dans le chantier de départ
        if materiel.chantier != chantier_depart:
            raise forms.ValidationError(f"{materiel.nom} n'est pas présent dans le chantier {chantier_depart.nom}.")

        # Vérifiez si la quantité disponible est suffisante
        if chantier_depart.quantite < quantite:
            raise forms.ValidationError(f"Quantité insuffisante dans le chantier {chantier_depart.nom}. Quantité disponible: {chantier_depart.quantite}")

        return cleaned_data
