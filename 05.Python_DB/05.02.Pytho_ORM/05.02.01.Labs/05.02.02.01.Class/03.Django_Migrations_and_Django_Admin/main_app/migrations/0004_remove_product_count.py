# Generated by Django 4.2.4 on 2023-11-07 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_product_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
    ]
