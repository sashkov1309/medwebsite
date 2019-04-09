from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('patient/', views.patient, name='patient'),
    path('patient/<int:patient_id>', views.patient_details, name='patientDetails'),

    path('lab/', views.lab, name='lab'),

    path('schedule/', views.schedule, name='schedule'),
]
