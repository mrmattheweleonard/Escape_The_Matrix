from django.db import models

# Create your models here.

class Episode(models.Model):

    number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="")
    date_aired = models.DateField(auto_now=True)
    episode_file = models.FileField(upload_to="episodes/", default="")