from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.patients, name='patients'),
    path('lab/', views.lab, name='lab'),
    path('schedule/', views.schedule, name='schedule'),
]
