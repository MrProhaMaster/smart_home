# Generated by Django 4.1.2 on 2024-02-07 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
