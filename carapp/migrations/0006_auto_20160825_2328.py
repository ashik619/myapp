# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0005_auto_20160825_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='dengine',
            field=models.CharField(default='nil', max_length=200),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='dpower',
            field=models.CharField(default='nil', max_length=200),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='dtorque',
            field=models.CharField(default='nil', max_length=200),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='dtransmission',
            field=models.CharField(default='nil', max_length=200),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='model_name',
            field=models.CharField(default='nil', max_length=100),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='pengine',
            field=models.CharField(default='nil', max_length=200),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='ppower',
            field=models.CharField(default='nil', max_length=200),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='ptorque',
            field=models.CharField(default='nil', max_length=200),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='ptransmission',
            field=models.CharField(default='nil', max_length=200),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='text',
            field=models.TextField(default='nil'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='type',
            field=models.CharField(default='nil', max_length=100),
        ),
    ]
