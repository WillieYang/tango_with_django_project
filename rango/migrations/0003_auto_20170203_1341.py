# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-03 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170201_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='Category',
            new_name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='DEFAULT VALUE', max_length=128),
        ),
    ]
