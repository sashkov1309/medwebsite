from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('patient/', views.patient, name='patient'),
    path('patient/<int:patient_id>', views.DetailView.as_view(), name='patient_details'),
    path('patient/<int:patient_id>/medtest/<int:medtest_id>', views.patient_details, name='medtest_details'),
    # path('lab/', views.lab, name='lab'),
    # path('schedule/', views.schedule, name='schedule'),
]
