from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Deplacement, Materiel

@receiver(post_save, sender=Deplacement)
def update_materiel_quantite(sender, instance, **kwargs):
    materiel = instance.materiel
    materiel.quantite -= instance.quantite
    if materiel.quantite < 0:
        raise ValueError("Quantité à déplacer dépasse la quantité disponible")
    materiel.save()

    # Vérifier si le matériel existe déjà dans le chantier de destination
    materiel_dest, created = Materiel.objects.get_or_create(
        chantier=instance.chantier_destination,
        designation=materiel.designation,
        defaults={
            'description': materiel.description,
            'prix_unit_ht': materiel.prix_unit_ht,
            'prix_unit_ttc': materiel.prix_unit_ttc,
            'prix_total_ttc': materiel.prix_total_ttc,
            'date_entree': materiel.date_entree,
            'note': materiel.note,
            'quantite': 0  # Initialiser à 0 si nouvellement créé
        }
    )
    materiel_dest.quantite += instance.quantite
    materiel_dest.save()
