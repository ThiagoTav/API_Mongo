# weatherapi/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from project.models import WeatherHistory
from project.historicoSerializers import WeatherHistorySerializer

class WeatherAPIView(APIView):
    def get(self, request, format=None):
        # Substitua a URL abaixo pela API externa real
        api_url = "https://api.exemplo.com/weather"

        try:
            response = requests.get(api_url)
            data = response.json()

            # Extrair os dados necessários
            temperature = data['temperature']
            pressure = data['pressure']
            humidity = data['humidity']
            precipitation = data['precipitation']
            condition = data['condition']

            # Salvar os dados no banco de dados local
            WeatherHistory.objects.create(
                temperature=temperature,
                pressure=pressure,
                humidity=humidity,
                precipitation=precipitation,
                condition=condition
            )

            # Serializar e retornar os dados
            serializer = WeatherHistorySerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)