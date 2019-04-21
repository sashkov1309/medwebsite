from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/', views.patient, name='patient'),
    path('patient/<int:patient_id>', views.patient_details, name='patient_details'),
    path('patient/<int:patient_id>/medtest/<int:medtest_id>', views.patient_details, name='medtest_details'),
    # path('lab/', views.lab, name='lab'),
    # path('schedule/', views.schedule, name='schedule'),
]
