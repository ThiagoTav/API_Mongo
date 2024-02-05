# weatherapi/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from project.models import WeatherHistory
from project.historicoSerializers import WeatherHistorySerializer

class WeatherAPIView(APIView):
    def get(self, request, format=None):
        try:
            # Definir os valores manualmente (substitua pelos valores desejados)
            temperature = 25.0
            pressure = 1015.0
            humidity = 60.0
            precipitation = 0.5
            condition = 'Sunny'

            # Salvar os dados no banco de dados local
            WeatherHistory.objects.create(
                temperature=temperature,
                pressure=pressure,
                humidity=humidity,
                precipitation=precipitation,
                condition=condition
            )

            # Serializar e retornar os dados
            serializer = WeatherHistorySerializer(data=WeatherHistory.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
