from django.urls import path

from .views import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
)

urlpatterns = [
    path('sensors/', ListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', RetrieveUpdateAPIView.as_view(), name='sensor-detail'),
    path('measurements/', CreateAPIView.as_view(), name='measurement-create'),
]
    # TODO: зарегистрируйте необходимые маршруты
