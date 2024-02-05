from django.urls import path
from project.views import WeatherAPIView

urlpatterns = [
    path('weather-history/', WeatherAPIView.as_view(), name='weather-history-list-create'),
]