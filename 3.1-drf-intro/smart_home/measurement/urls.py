from django.urls import path
from .views import (
    SensorListCreateView,
    SensorRetrieveUpdateView,
    MeasurementCreateView,
)

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),                  # GET, POST
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view()),    # GET, PATCH
    path('measurements/', MeasurementCreateView.as_view()),           # POST
]
