import requests
from rest_framework import generics
from rest_framework.response import Response
from .models import WeatherHistory
from project.historicoSerializers import WeatherHistorySerializer

class WeatherHistoryListCreateView(generics.ListCreateAPIView):
    queryset = WeatherHistory.objects.all()
    serializer_class = WeatherHistorySerializer

    def get_queryset(self):
        return WeatherHistory.objects.all()

    def create(self, request, *args, **kwargs):
        external_data = self.get_external_weather_data()
        weather_history = WeatherHistory.objects.create(
            timestamp=external_data['timestamp'],
            temperature=external_data['temperature'],
            pressure=external_data['pressure'],
            humidity=external_data['humidity'],
            precipitation=external_data['precipitation'],
            condition=external_data['condition'],
        )

        serializer = WeatherHistorySerializer(weather_history)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def get_external_weather_data(self):
        api_key = 'dfd9ffed5be4eacd9d85e5e8aa360a7a'
        city = 'Sorocaba'
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        response = requests.get(base_url)
        data = response.json()

        external_data = {
            'timestamp': data['dt'],
            'temperature': data['main']['temp'],
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'precipitation': 0,  # Infelizmente, a API OpenWeatherMap não fornece essa informação gratuitamente
            'condition': data['weather'][0]['description'],
        }

        return external_data
