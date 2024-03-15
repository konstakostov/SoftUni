# Generated by Django 4.2.4 on 2023-11-15 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_menureview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodcriticrestaurantreview',
            options={'ordering': ['-rating'], 'verbose_name': 'Food Critic Review', 'verbose_name_plural': 'Food Critic Reviews'},
        ),
        migrations.AlterUniqueTogether(
            name='foodcriticrestaurantreview',
            unique_together={('reviewer_name', 'restaurant')},
        ),
    ]
