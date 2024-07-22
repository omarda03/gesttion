from django.db import models, transaction
from django.core.exceptions import ValidationError

class Chantier(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.TextField()

    def __str__(self):
        return self.nom

class Materiel(models.Model):
    chantier = models.ForeignKey(Chantier, related_name='materiels', on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantite = models.IntegerField()
    prix_unit_ht = models.DecimalField(max_digits=10, decimal_places=2)
    prix_unit_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    prix_total_ttc = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    date_entree = models.DateField()
    note = models.TextField()

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        self.prix_total_ttc = self.prix_unit_ttc * self.quantite
        super().save(*args, **kwargs)
        if self.quantite == 0:
            self.delete()

class Deplacement(models.Model):
    chantier_depart = models.ForeignKey(Chantier, related_name='departs', on_delete=models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantite = models.IntegerField()
    chantier_destination = models.ForeignKey(Chantier, related_name='destinations', on_delete=models.CASCADE)
    date_deplacement = models.DateField()

    def __str__(self):
        return f'{self.materiel.designation} de {self.chantier_depart.nom} à {self.chantier_destination.nom}'

    def save(self, *args, **kwargs):
        if self.pk is None:  # Only validate for new records
            if self.quantite > self.materiel.quantite:
                raise ValidationError("Quantité à déplacer dépasse la quantité disponible")
            with transaction.atomic():
                self.update_materiel_quantite()
        super().save(*args, **kwargs)

    def update_materiel_quantite(self):
        with transaction.atomic():
            # Verrouillez la ligne Materiel pour éviter les conditions de concurrence
            materiel_depart = Materiel.objects.select_for_update().get(pk=self.materiel.pk)
            if materiel_depart.quantite < self.quantite:
                raise ValidationError("Quantité à déplacer dépasse la quantité disponible")
            materiel_depart.quantite -= self.quantite
            materiel_depart.save()

            materiel_destination, created = Materiel.objects.select_for_update().get_or_create(
                chantier=self.chantier_destination,
                designation=self.materiel.designation,
                defaults={
                    'quantite': self.quantite,
                    'prix_unit_ht': self.materiel.prix_unit_ht,
                    'prix_unit_ttc': self.materiel.prix_unit_ttc,
                    'prix_total_ttc': self.materiel.prix_unit_ttc * self.quantite,
                    'date_entree': self.materiel.date_entree,
                    'note': self.materiel.note,
                }
            )

            if not created:
                materiel_destination.quantite += self.quantite

            materiel_destination.prix_total_ttc = materiel_destination.prix_unit_ttc * materiel_destination.quantite
            materiel_destination.save()
