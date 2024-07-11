# Generated by Django 5.0.6 on 2024-07-11 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deplacement', '0002_materiel_nom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deplacement',
            name='description',
        ),
        migrations.RemoveField(
            model_name='materiel',
            name='date_entree',
        ),
        migrations.RemoveField(
            model_name='materiel',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='materiel',
            name='note',
        ),
        migrations.RemoveField(
            model_name='materiel',
            name='prix_total_ttc',
        ),
        migrations.RemoveField(
            model_name='materiel',
            name='prix_unit_ht',
        ),
        migrations.RemoveField(
            model_name='materiel',
            name='prix_unit_ttc',
        ),
        migrations.AddField(
            model_name='chantier',
            name='quantite',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='materiel',
            name='chantier',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='deplacement.chantier'),
        ),
        migrations.AlterField(
            model_name='chantier',
            name='localisation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='deplacement',
            name='chantier_depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='deplacement.chantier'),
        ),
        migrations.AlterField(
            model_name='deplacement',
            name='chantier_destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='deplacement.chantier'),
        ),
        migrations.AlterField(
            model_name='deplacement',
            name='date_deplacement',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='nom',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='quantite',
            field=models.IntegerField(default=0),
        ),
    ]
