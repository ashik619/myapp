# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='engine',
            field=models.CharField(max_length=200),
        ),
    ]
