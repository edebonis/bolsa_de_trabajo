# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-09-18 22:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa', '0004_auto_20190918_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='fecha',
            field=models.DateField(default=datetime.date(2019, 9, 18)),
        ),
    ]
