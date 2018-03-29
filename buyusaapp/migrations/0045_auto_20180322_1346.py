# Generated by Django 2.0.2 on 2018-03-22 05:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyusaapp', '0044_auto_20180321_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('C5', 'Category 5'), ('C3', 'Category 3'), ('C4', 'Category 4'), ('C1', 'Category 1'), ('C2', 'Category 2')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='gig',
            name='description',
            field=ckeditor.fields.RichTextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CompanyType',
            field=models.CharField(choices=[('independent', 'Independent'), ('retail', 'Retail'), ('manufacturer', 'Manufacturer'), ('wholesale', 'Wholesale'), ('service', 'Service')], default='manufacturer', max_length=12),
        ),
    ]
