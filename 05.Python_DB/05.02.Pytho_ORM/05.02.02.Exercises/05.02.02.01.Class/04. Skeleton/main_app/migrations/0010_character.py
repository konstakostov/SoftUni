# Generated by Django 4.2.6 on 2023-10-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_hotelroom_room_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_name', models.CharField(choices=[('Mage', 'Mage'), ('Warrior', 'Warrior'), ('Assassin', 'Assassin'), ('Scout', 'Scout')], max_length=100)),
                ('level', models.PositiveIntegerField()),
                ('strength', models.PositiveIntegerField()),
                ('dexterity', models.PositiveIntegerField()),
                ('intelligence', models.PositiveIntegerField()),
                ('hit_points', models.PositiveIntegerField()),
                ('inventory', models.TextField()),
            ],
        ),
    ]
