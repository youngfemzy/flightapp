# Generated by Django 5.0.7 on 2024-07-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0002_remove_airline_seats_airline_capacity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='phone',
        ),
        migrations.AddField(
            model_name='airline',
            name='takeoff_date',
            field=models.DateTimeField(null=True),
        ),
    ]
