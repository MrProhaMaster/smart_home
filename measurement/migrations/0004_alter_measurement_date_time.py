# Generated by Django 4.1.2 on 2024-02-07 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
