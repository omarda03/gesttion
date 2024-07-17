from django.db import models
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
    prix_total_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    date_entree = models.DateField()
    note = models.TextField()

    def __str__(self):
        return self.designation

class Deplacement(models.Model):
    chantier_depart = models.ForeignKey(Chantier, related_name='departs', on_delete=models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantite = models.IntegerField()
    chantier_destination = models.ForeignKey(Chantier, related_name='destinations', on_delete=models.CASCADE)
    date_deplacement = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.materiel.designation} de {self.chantier_depart.nom} à {self.chantier_destination.nom}'

    def save(self, *args, **kwargs):
        print(f'Appel de save pour {self} avec quantité {self.quantite}')
        if self.quantite > self.materiel.quantite:
            raise ValidationError("Quantité à déplacer dépasse la quantité disponible")

        if self.pk is None:
            print('Ceci est une nouvelle instance')
        else:
            print('Ceci est une mise à jour de l\'instance')

        super().save(*args, **kwargs)
        self.update_materiel_quantite()

    def update_materiel_quantite(self):
        print(f'Quantité initiale dans le chantier de départ : {self.materiel.quantite}')
        self.materiel.quantite -= self.quantite
        print(f'Quantité après soustraction dans le chantier de départ : {self.materiel.quantite}')
        self.materiel.save()

        materiel_destination, created = Materiel.objects.get_or_create(
            chantier=self.chantier_destination,
            designation=self.materiel.designation,
            defaults={
                'quantite': 0,
                'prix_unit_ht': self.materiel.prix_unit_ht,
                'prix_unit_ttc': self.materiel.prix_unit_ttc,
                'prix_total_ttc': self.materiel.prix_total_ttc,
                'date_entree': self.materiel.date_entree,
                'note': self.materiel.note
            }
)

        if not created:
            print(f'Quantité initiale dans le chantier de destination (avant ajout) : {materiel_destination.quantite}')
            materiel_destination.quantite += self.quantite
            print(f'Quantité après ajout dans le chantier de destination : {materiel_destination.quantite}')
        else:
            materiel_destination.quantite = self.quantite
            print(f'Quantité nouvelle dans le chantier de destination (créé) : {materiel_destination.quantite}')

        materiel_destination.save()
