from django.urls import path
from project.views import WeatherHistoryListCreateView

urlpatterns = [
    path('weather-history/', WeatherHistoryListCreateView.as_view(), name='weather-history-list-create'),
]