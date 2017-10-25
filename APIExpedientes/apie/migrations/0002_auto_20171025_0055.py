# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actualizacion',
            old_name='Fecha de recibido',
            new_name='fecha_envio',
        ),
        migrations.RenameField(
            model_name='actualizacion',
            old_name='Fecha enviado',
            new_name='fecha_recibido',
        ),
        migrations.RenameField(
            model_name='expediente',
            old_name='Fecha de entrada',
            new_name='fecha_entrada',
        ),
        migrations.RemoveField(
            model_name='expediente',
            name='Fecha de finalizacion',
        ),
        migrations.AddField(
            model_name='expediente',
            name='fecha_finalizacion',
            field=models.DateField(default=None),
        ),
    ]