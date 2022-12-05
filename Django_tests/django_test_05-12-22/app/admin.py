from django.contrib import admin
from .models import Sensor
from .models import DataRecords

admin.site.register(Sensor)
admin.site.register(DataRecords)
