from rest_framework import serializers
from project.models import Clima


class ClimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clima
        fields = ('cidade', 'temperatura', 'condicao', 'data_hora')

