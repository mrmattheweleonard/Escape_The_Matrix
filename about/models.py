from django.db import models

# Create your models here.

class About(models.Model):
    about_paragraph = models.TextField(max_length=1000, default="")