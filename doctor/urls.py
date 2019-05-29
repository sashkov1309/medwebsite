from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('patient/', views.PatientsView.as_view(), name='patients'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient_details'),
    path('patient/add', views.PatientCreate.as_view(), name='create_patient'),
    path('patient/<int:pk>/update', views.PatientUpdate.as_view(), name='update_patient'),
    path('patient/<int:pk>/delete', views.PatientDelete.as_view(), name='delete_patient'),

    path('patient/<int:pk>/medtest/', views.MedicalTestsView.as_view(), name='medtests'),

    path('patient/<int:pk>/medtest/<int:medpk>', views.MedicalTestsDetailView.as_view(), name='medtest_details'),
    path('patient/<int:pk>/medrefferal/', views.MedicalTestCreate.as_view(), name='medrefferal'),

    path('schedule/<int:pk>', views.WeekView.as_view(), name='schedule'),
    path('schedule/apply/<int:pk>', views.ApplyForVisitView.as_view(), name='apply_for_visit'),

    path('userform/', views.UserFormView.as_view(), name='userform'),
]
