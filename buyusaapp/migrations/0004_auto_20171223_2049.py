# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-12-23 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyusaapp', '0003_auto_20171222_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('C3', 'Category 3'), ('C2', 'Category 2'), ('C1', 'Category 1'), ('C5', 'Category 5'), ('C4', 'Category 4')], max_length=2),
        ),
    ]
