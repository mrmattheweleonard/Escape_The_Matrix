from django.db import models

# Create your models here.


class Home(models.Model):
    # welcome_paragraph will be added to admin so any admin can update the welcome text displayed on the home page. 
    welcome_paragraph = models.TextField(max_length=1000, default='')
