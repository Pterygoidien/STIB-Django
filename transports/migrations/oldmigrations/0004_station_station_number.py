# Generated by Django 4.0 on 2021-12-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0003_line_line_stations'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='Station_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
