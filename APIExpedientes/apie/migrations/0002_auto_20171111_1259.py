# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualizacion',
            name='fecha_envio',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='actualizacion',
            name='fecha_recibido',
            field=models.DateTimeField(null=True),
        ),
    ]