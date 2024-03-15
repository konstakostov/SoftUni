# Generated by Django 4.2.4 on 2023-11-13 16:24

from django.db import migrations
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_veterinarian_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinarian',
            name='availability',
            field=main_app.models.BooleanChoiceField(choices=[(True, 'Available'), (False, 'Not Available')], default=True),
        ),
    ]
