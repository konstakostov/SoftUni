# Generated by Django 4.2.4 on 2023-11-15 14:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_restaurantreview_regularrestaurantreview_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_content', models.TextField()),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.menu')),
            ],
            options={
                'verbose_name': 'Menu Review',
                'verbose_name_plural': 'Menu Reviews',
                'ordering': ['-rating'],
                'indexes': [models.Index(fields=['menu'], name='main_app_menu_review_menu_id')],
                'unique_together': {('reviewer_name', 'menu')},
            },
        ),
    ]
