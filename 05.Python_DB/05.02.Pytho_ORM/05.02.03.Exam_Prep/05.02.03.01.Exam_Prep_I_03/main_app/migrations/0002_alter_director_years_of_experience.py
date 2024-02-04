# Generated by Django 4.2.4 on 2023-11-25 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='years_of_experience',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
