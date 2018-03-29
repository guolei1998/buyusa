# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-01-28 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyusaapp', '0034_auto_20180128_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gig',
            old_name='photo',
            new_name='BrandPicture1',
        ),
        migrations.RemoveField(
            model_name='gig',
            name='price',
        ),
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('C5', 'Category 5'), ('C4', 'Category 4'), ('C2', 'Category 2'), ('C1', 'Category 1'), ('C3', 'Category 3')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CompanyCategory',
            field=models.CharField(choices=[('b2b', 'Business-to-Business'), ('b2c', 'Business-to-Consumer')], default='b2c', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CompanyType',
            field=models.CharField(choices=[('retail', 'Retail'), ('manufacturer', 'Manufacturer'), ('service', 'Service'), ('wholesale', 'Wholesale'), ('independent', 'Independent')], default='manufacturer', max_length=12),
        ),
    ]
