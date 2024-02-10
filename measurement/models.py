from django.db import models
from datetime import datetime

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    sensor_id = models.ForeignKey("Sensor", on_delete=models.CASCADE)
    temperature = models.FloatField()
    date_time = models.DateTimeField(default=datetime.now)
