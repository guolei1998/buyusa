# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-01-02 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyusaapp', '0017_auto_20171231_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('C3', 'Category 3'), ('C5', 'Category 5'), ('C4', 'Category 4'), ('C1', 'Category 1'), ('C2', 'Category 2')], max_length=2),
        ),
    ]
