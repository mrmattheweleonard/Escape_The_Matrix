from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Home

# Create your views here.

class HomePageView(ListView):
    model = Home
    template_name = "home.html"