from django.shortcuts import render
from .models import Bot


def home(request):
    bots = Bot.objects.all()
    return render(request, 'content/home.html', {'bots': bots})


def about(request):
    return render(request, 'content/about.html', {'title': 'About'})
