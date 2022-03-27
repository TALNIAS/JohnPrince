from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_Title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.ImageField()