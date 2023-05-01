# Generated by Django 4.1.7 on 2023-05-01 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tc2005', '0015_authregistro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesession',
            name='playerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]