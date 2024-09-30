# Generated by Django 5.1.1 on 2024-09-30 02:02

import django.core.validators
import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[petstagram.photos.validators.FileSizeValidator(5)])),
                ('description', models.TextField(blank=True, max_length=300, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(max_length=30)),
                ('date_of_publication', models.DateTimeField(auto_now_add=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, to='pets.pet')),
            ],
        ),
    ]
