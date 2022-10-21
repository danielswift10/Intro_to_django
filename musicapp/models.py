from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()
    
class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateField()
    likes = models.CharField(max_length=200)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
class Lyric(models.Model):
    content = models.CharField(max_length=400)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)