from rest_framework import serializers
from .models import Artiste, Song, Lyric


class ArtisteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Artiste
        fields = "__all__"


class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class LyricSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = "__all__"
