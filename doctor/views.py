from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>index</h1>")


def patients(request):
    return HttpResponse("<h1>patients</h1>")


def lab(request):
    return HttpResponse("<h1>lab</h1>")


def schedule(request):
    return HttpResponse("<h1>schedule</h1>")
