from rest_framework.views import APIView
from rest_framework.response import Response
from project.historicoSerializers import ClimaSerializer
import requests
from project.models import Clima
from rest_framework import status
from rest_framework import generics


class ClimaAPIView(APIView):
    def get(self, request):
        cidade = request.query_params.get('cidade')

        if cidade:
            # Chamada para API OpenWeatherMap
            url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=dfd9ffed5be4eacd9d85e5e8aa360a7a'
            response = requests.get(url)
            data = response.json()

            # Extrair dados relevantes
            temperatura = data['main']['temp']
            condicao = data['weather'][0]['description']

            # Criar novo objeto Clima
            clima = Clima.objects.create(
                cidade=cidade,
                temperatura=temperatura,
                condicao=condicao,
            )

            # Serializar objeto Clima para JSON
            serializer = ClimaSerializer(clima)

            return Response(serializer.data)
        else:
            return Response({"message": "O parâmetro 'cidade' não foi fornecido na query da URL."}, status=status.HTTP_400_BAD_REQUEST)
        

class ClimaDetailAPIView(generics.RetrieveAPIView):
    queryset = Clima.objects.all()
    serializer_class = ClimaSerializer
    lookup_field = 'pk'

class ClimaListAPIView(generics.ListAPIView):
    queryset = Clima.objects.all()
    serializer_class = ClimaSerializer