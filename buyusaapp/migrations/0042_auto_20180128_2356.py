# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-01-28 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyusaapp', '0041_auto_20180128_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('C1', 'Category 1'), ('C3', 'Category 3'), ('C5', 'Category 5'), ('C4', 'Category 4'), ('C2', 'Category 2')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CompanyType',
            field=models.CharField(choices=[('independent', 'Independent'), ('retail', 'Retail'), ('service', 'Service'), ('wholesale', 'Wholesale'), ('manufacturer', 'Manufacturer')], default='manufacturer', max_length=12),
        ),
    ]
