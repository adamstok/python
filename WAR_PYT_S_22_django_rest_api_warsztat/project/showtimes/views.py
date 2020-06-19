from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework import viewsets
from showtimes.models import Screening, Cinema
from showtimes.serializers import CinemaSerializer, ScreeninSerializer

# Create your views here.
class CinemaViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class ScreeningViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeninSerializer



