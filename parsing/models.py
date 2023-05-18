from django.db import models

# Create your models here.

class Anime(models.Model):
    title = models.CharField(max_length=250)
    release_data = models.DateField(auto_now=True)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
