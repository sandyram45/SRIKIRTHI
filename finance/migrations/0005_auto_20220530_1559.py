# Generated by Django 3.2.13 on 2022-05-30 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_salaryexpenses_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleexpenses',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vehicleexpenses',
            name='vehicle_number',
            field=models.CharField(choices=[('TN59BH0475', 'TN59BH0475')], max_length=10),
        ),
    ]
