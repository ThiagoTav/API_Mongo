from django.urls import path
from project.views import ClimaAPIView, ClimaDetailAPIView, ClimaListAPIView

urlpatterns = [
    path('history/', ClimaAPIView.as_view(), name='clima-list-create'),
    path('history/<int:pk>/', ClimaDetailAPIView.as_view(), name='clima-detail'),
    path('history/all/', ClimaListAPIView.as_view(), name='clima-list'),
]