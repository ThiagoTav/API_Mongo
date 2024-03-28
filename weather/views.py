from datetime import datetime
from random import randrange
from django.shortcuts import render, redirect
from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherSerializer
from .forms import WeatherForm
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

class WeatherView(View):
    def get(self, request):
        verse = main.get_bible_verse()
        repository = WeatherRepository(collectionName='weathers')
        weathers = list(repository.getAll())
        serializer = WeatherSerializer(data=weathers, many=True)
        if serializer.is_valid():
            modelWeather = serializer.save()
            print(serializer.data)
        else:
            print(serializer.errors)
        return render(request, "home.html", {"weathers": weathers, "verse": verse})
    

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather = WeatherEntity(
            temperature=randrange(start=17, stop=40),
            date=datetime.now(),
            city='Sorocaba'
        )
        repository.insert(weather.__dict__)
        return redirect('Weather View')
    
class WeatherReset(View):
    def get(self, request): 
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteAll()
        return redirect('Weather View')
    
class WeatherInsert(View):
    def get(self, request):
        weatherForm = WeatherForm()
        return render(request, "form.html", {"form": weatherForm})
    
    def post(self, request):
        weatherForm = WeatherForm(request.POST)
        if weatherForm.is_valid():
            repository = WeatherRepository(collectionName='weathers')
            repository.insert(weatherForm.cleaned_data)
        else:
            print(weatherForm.errors)
        return redirect('Weather View')