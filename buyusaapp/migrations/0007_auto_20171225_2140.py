# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-12-25 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyusaapp', '0006_auto_20171225_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('C2', 'Category 2'), ('C1', 'Category 1'), ('C5', 'Category 5'), ('C3', 'Category 3'), ('C4', 'Category 4')], max_length=2),
        ),
    ]