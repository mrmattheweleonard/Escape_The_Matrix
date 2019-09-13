from django.shortcuts import render
from django.views.generic import TemplateView
from .models import About

class AboutUsView(TemplateView):
    model = About
    template_name = "about.html"
