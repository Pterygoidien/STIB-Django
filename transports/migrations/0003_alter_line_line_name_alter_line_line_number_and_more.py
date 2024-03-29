# Generated by Django 4.0 on 2021-12-20 20:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0002_auto_20211220_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='Line_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nom de la ligne (départ-arrivée)'),
        ),
        migrations.AlterField(
            model_name='line',
            name='Line_number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Numéro de la ligne'),
        ),
        migrations.AlterField(
            model_name='route',
            name='order',
            field=models.IntegerField(verbose_name='Ordre de passage'),
        ),
        migrations.AlterField(
            model_name='station',
            name='Station_adress',
            field=models.CharField(max_length=300, verbose_name="Adresse de l'arret"),
        ),
        migrations.AlterField(
            model_name='station',
            name='Station_desc',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Description (ou tag Google Map)'),
        ),
        migrations.AlterField(
            model_name='station',
            name='Station_name',
            field=models.CharField(max_length=200, verbose_name="Nom de l'arrêt"),
        ),
        migrations.AlterField(
            model_name='station',
            name='Station_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Identification (facultatif)'),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='vehicule_type',
            field=models.CharField(choices=[('B', 'Bus'), ('T', 'Tram'), ('M', 'Metro'), ('N', 'Noctis')], default='B', max_length=1, verbose_name='type de véhicule'),
        ),
    ]
