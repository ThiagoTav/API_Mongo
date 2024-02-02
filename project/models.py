from django.db import models

class WeatherHistory(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()
    condition = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.timestamp} - {self.condition}'