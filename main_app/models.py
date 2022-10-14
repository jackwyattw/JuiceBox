from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Track(models.Model):

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    duration = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    lyrics = models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class Playlist(models.Model):

    title = models.CharField(max_length=150)

    # create join table
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.title
