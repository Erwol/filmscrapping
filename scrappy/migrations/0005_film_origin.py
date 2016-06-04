# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrappy', '0004_remove_film_last_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='origin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scrappy.Origin'),
            preserve_default=False,
        ),
    ]
