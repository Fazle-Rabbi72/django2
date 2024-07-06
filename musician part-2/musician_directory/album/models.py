from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    musician = models.ForeignKey(Musician, related_name='albums', on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    RATING_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.album_name