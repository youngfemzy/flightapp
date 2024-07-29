# Generated by Django 5.0.7 on 2024-07-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0007_alter_airline_seats_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderflight',
            name='totalbill',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='orderflight',
            name='totalseatsbooked',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='capacity',
            field=models.IntegerField(blank=True, default=240, null=True),
        ),
    ]