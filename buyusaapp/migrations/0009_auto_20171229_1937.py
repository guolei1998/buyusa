# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-12-29 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyusaapp', '0008_auto_20171225_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('C3', 'Category 3'), ('C1', 'Category 1'), ('C4', 'Category 4'), ('C2', 'Category 2'), ('C5', 'Category 5')], max_length=2),
        ),
    ]
