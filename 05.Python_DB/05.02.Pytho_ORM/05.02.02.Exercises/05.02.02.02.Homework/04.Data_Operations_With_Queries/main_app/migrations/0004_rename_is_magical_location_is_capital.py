# Generated by Django 4.2.4 on 2023-11-20 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='is_magical',
            new_name='is_capital',
        ),
    ]
