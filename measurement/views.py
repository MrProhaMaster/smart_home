# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer

class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class ListMCreateAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorDetailSerializer

class CreateSAPIView(APIView):
    def post(self, request):
            recievedData = request.data
            new_sensor = SensorDetailSerializer(data=recievedData)
            if new_sensor.is_valid():
                new_sensor.save()
                return Response(new_sensor.data)
            else:
                return Response()

class RetrieveUpdateAPIView(APIView):
    def patch(self, request):
            recievedData = request.data
            pk = recievedData['id']
            patchSensor = Sensor.objects.get(pk=pk)
            update_sensor = SensorDetailSerializer(patchSensor, recievedData, partial=True)
            if update_sensor.is_valid():
                update_sensor.save()
                return Response(update_sensor.data)

class CreateMAPIView(APIView):
    def post(self, request):
        recievedData = request.data
        new_measure = Measurement(data=recievedData)
        if new_measure.is_valid():
            new_measure.save()
            return Response(new_measure.data)
        else:
            return Response()

