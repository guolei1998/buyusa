# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-12-30 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyusaapp', '0012_auto_20171230_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('C1', 'Category 1'), ('C4', 'Category 4'), ('C3', 'Category 3'), ('C2', 'Category 2'), ('C5', 'Category 5')], max_length=2),
        ),
    ]
