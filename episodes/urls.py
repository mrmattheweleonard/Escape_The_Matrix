from django.urls import path
from . import views

urlpatterns = [
    path("episodes/", views.EpisodePageView.as_view(), name="episodes"),
    path("episodes/episode_detail", views.EpisodeDetailView.as_view(), name="episode_detail"),
]