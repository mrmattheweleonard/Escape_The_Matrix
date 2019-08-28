from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Episode

# Create your views here.

class EpisodePageView(ListView):
    model = Episode
    template_name = "episodes.html"
    context_object_name = 'episodes'

class EpisodeDetailView(TemplateView):
    model = Episode
    template_name = "episode_detail.html"