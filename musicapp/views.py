from django.shortcuts import render
from .serializers import ArtisteSerializers, SongSerializers, LyricSerializers
from rest_framework import viewsets
from .models import Artiste, Song, Lyric


class ArtisteViewsets(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializers


class SongViewsets(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers
