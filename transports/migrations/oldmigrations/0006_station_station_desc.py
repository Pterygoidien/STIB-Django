# Generated by Django 4.0 on 2021-12-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0005_alter_station_station_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='Station_desc',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
