from .models import Sensor
from .models import DataRecords
from .serializers import SensorSerializer
from .serializers import DataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .filters import SensorDataFilter
from django.shortcuts import render


class SensorAPI:

    @staticmethod
    @api_view(["GET", "POST"])
    def sensor_list(request):

        if request.method == "GET":
            sensors = Sensor.objects.all()
            serializer = SensorSerializer(sensors, many=True)
            return Response(serializer.data)

        elif request.method == "POST":
            serializer = SensorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    @api_view(["GET", "PUT", "DELETE"])
    def sensor_info(request, id):

        try:
            sensor = Sensor.objects.get(id=id)
        except Sensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            serializer = SensorSerializer(sensor)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = SensorSerializer(sensor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            sensor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class DataAPI:

    @staticmethod
    @api_view(["GET", "POST"])
    def data_list(request):

        if request.method == "GET":
            sensor_filter = SensorDataFilter(request.GET, queryset=DataRecords.objects.all())
            return render(request, "filter_view.html", {"filter": sensor_filter})

        elif request.method == "POST":
            serializer = DataSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    @api_view(["GET", "PUT", "DELETE"])
    def data_info(request, id):

        try:
            data_records = DataRecords.objects.get(id=id)
        except DataRecords.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            serializer = DataSerializer(data_records)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = DataSerializer(data_records, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            data_records.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

