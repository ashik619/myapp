# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-23 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0006_auto_20160825_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='nil', max_length=100)),
                ('dengine', models.CharField(default='nil', max_length=200)),
                ('dpower', models.CharField(default='nil', max_length=200)),
                ('dtorque', models.CharField(default='nil', max_length=200)),
                ('dtransmission', models.CharField(default='nil', max_length=200)),
                ('pengine', models.CharField(default='nil', max_length=200)),
                ('ppower', models.CharField(default='nil', max_length=200)),
                ('ptorque', models.CharField(default='nil', max_length=200)),
                ('ptransmission', models.CharField(default='nil', max_length=200)),
                ('text', models.TextField(default='nil')),
            ],
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='dengine',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='dpower',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='dtorque',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='dtransmission',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='pengine',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='ppower',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='ptorque',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='ptransmission',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='text',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='type',
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='model_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='cardetails',
            name='carmodel_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carapp.CarModel'),
        ),
    ]
