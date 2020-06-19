from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from rest_framework.permissions import IsAuthenticated

from movielist.models import Movie, Person
from movielist.serializers import MovieSerializer, PersonSerializer
from rest_framework import generics, viewsets, request


# class MovieListView(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# class MovieView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


class MovieViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class PersonViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

