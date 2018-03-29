# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-13 23:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyusaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('C2', 'Category 2'), ('C5', 'Category 5'), ('C3', 'Category 3'), ('C1', 'Category 1'), ('C4', 'Category 4')], max_length=2)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField(default=6)),
                ('photo', models.FileField(upload_to='gigs')),
                ('status', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
