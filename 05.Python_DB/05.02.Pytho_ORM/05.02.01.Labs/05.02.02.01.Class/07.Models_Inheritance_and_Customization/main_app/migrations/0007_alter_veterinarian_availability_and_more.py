# Generated by Django 4.2.4 on 2023-11-13 16:21

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_veterinarian_license_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinarian',
            name='availability',
            field=main_app.models.BooleanChoiceField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='veterinarian',
            name='license_number',
            field=models.CharField(max_length=10),
        ),
    ]
