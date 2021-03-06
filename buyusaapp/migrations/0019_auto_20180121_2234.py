# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-01-21 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buyusaapp', '0018_auto_20180102_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='BrandLink',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='gig',
            name='BrandLogo',
            field=models.FileField(default='', upload_to='gigs'),
        ),
        migrations.AddField(
            model_name='gig',
            name='BrandPicture2',
            field=models.FileField(default='', upload_to='gigs'),
        ),
        migrations.AddField(
            model_name='gig',
            name='BrandPicture3',
            field=models.FileField(default='', upload_to='gigs'),
        ),
        migrations.AddField(
            model_name='gig',
            name='BrandPicture4',
            field=models.FileField(default='', upload_to='gigs'),
        ),
        migrations.AddField(
            model_name='gig',
            name='BrandPicture5',
            field=models.FileField(default='', upload_to='gigs'),
        ),
        migrations.AddField(
            model_name='gig',
            name='BrandSearch',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='gig',
            name='BrandWhereToBuy',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='BBB',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='CompanyCategory',
            field=models.CharField(choices=[('b2b', 'Business-to-Business'), ('b2c', 'Business-to-Consumer')], default='b2c', max_length=3),
        ),
        migrations.AddField(
            model_name='profile',
            name='CompanyContactEmail',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='CompanyContactName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='CompanyContactPhone',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='CompanyJoined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='CompanyLink',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='CompanyLogo',
            field=models.FileField(default='', upload_to='profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='CompanyName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='CompanyType',
            field=models.CharField(choices=[('wholesale', 'Wholesale'), ('independent', 'Independent'), ('retail', 'Retail'), ('service', 'Service'), ('manufacturer', 'Manufacturer')], default='manufacturer', max_length=12),
        ),
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('C3', 'Category 3'), ('C2', 'Category 2'), ('C1', 'Category 1'), ('C5', 'Category 5'), ('C4', 'Category 4')], max_length=2),
        ),
    ]
