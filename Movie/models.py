from django.db import models

# Create your models here.
from Account.models import BaseUser


# iterable
Poster_CHOICES =(
    ("master", "master"),
    ("slave", "slave"),
)
class MoviePoster(BaseUser):
    bg_type = models.CharField(max_length=250, choices=Poster_CHOICES)  # "img/video",
    header = models.CharField(max_length=250, blank=True, null=True)  # "string_var",
    sub_header = models.CharField(max_length=250, blank=True, null=True)  # "string_var",
    alt_tag = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='poster')


class Movie(BaseUser):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    movie_path = models.FileField(upload_to='Movie')
    poster_id = models.ForeignKey(MoviePoster, on_delete=models.CASCADE)
