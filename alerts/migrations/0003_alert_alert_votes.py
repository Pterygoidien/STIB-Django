# Generated by Django 4.0 on 2021-12-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='alert_votes',
            field=models.IntegerField(default=0),
        ),
    ]