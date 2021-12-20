# Generated by Django 4.0 on 2021-12-20 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_utilisateur_phone_number'),
        ('alerts', '0003_alert_alert_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_timestamp', models.DateTimeField(auto_now=True)),
                ('vote_remark', models.TextField(blank=True, null=True)),
                ('alert_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerts.alert')),
                ('vote_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.utilisateur')),
            ],
        ),
    ]