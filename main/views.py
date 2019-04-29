from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})


def login(request):
    return render(request, 'registration/login.html', {})


def info(request):
    return render(request, 'main/info.html', {})
