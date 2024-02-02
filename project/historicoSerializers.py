from rest_framework import serializers
from .models import WeatherHistory

class WeatherHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherHistory
        fields = '__all__'