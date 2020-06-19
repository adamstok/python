from movielist.models import Movie, Person
from movielist.serializers import MovieSerializer, PersonSerializer
from rest_framework import generics, viewsets


# class MovieListView(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# class MovieView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer