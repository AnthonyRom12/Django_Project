from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='vibe-home'),
    path('about/', views.about, name='vibe-about'),
]
