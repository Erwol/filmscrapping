# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrappy', '0005_film_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='last_score',
            field=models.IntegerField(default=5),
        ),
    ]