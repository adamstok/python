from showtimes.models import Screening,Cinema
from rest_framework import serializers

class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = ['name','city','movies']

class ScreeninSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Screening
        fields = ['movie','cinema','date']

