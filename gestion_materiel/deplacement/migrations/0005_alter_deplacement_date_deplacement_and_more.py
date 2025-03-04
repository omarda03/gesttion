# Generated by Django 5.0.6 on 2024-07-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deplacement', '0004_alter_materiel_chantier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deplacement',
            name='date_deplacement',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='prix_total_ttc',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
    ]
