from django.db import models
from datetime import datetime


class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateField(default=datetime.now)
    likes = models.CharField(max_length=200)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.CharField(max_length=400)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
