from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('patient/', views.PatientsView.as_view(), name='patients'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient_details'),
    path('patient/<int:pk>/medtest/', views.MedicalTestsView.as_view(), name='medtests'),
    path('patient/<int:pk>/medtest/<int:medpk>', views.MedicalTestsDetailView.as_view(), name='medtest_details'),
    path('schedule/<int:pk>', views.ScheduleView.as_view(), name='schedule'),
]
