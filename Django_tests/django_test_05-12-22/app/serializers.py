from rest_framework import serializers
from .models import Sensor
from .models import DataRecords


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id", "name", "unit"]


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRecords
        fields = ["id", "sensor", "value", "date"]
