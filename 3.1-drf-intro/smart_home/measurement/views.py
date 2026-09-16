# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics

from .models import Sensor, Measurement
from .serializers import (
    SensorSerializer,
    SensorDetailSerializer,
    MeasurementSerializer,
)


class ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class RetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        # Для чтения — с измерениями, для изменения — краткий
        if self.request.method == 'GET':
            return SensorDetailSerializer
        return SensorSerializer


class CreateAPIView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer