# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 01:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('light_user', '0001_initial'),
        ('tasks', '0004_auto_20160915_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='light_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='light_user.LightUser'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
