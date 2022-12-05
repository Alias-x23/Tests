from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DataRecords(models.Model):
    sensor = models.CharField(max_length=100)
    date = models.DateTimeField(db_column="timestamp")
    value = models.DecimalField(decimal_places=20, max_digits=30)

    def __str__(self):
        return f"{self.sensor} - {self.date}"
