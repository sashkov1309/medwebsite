from django.urls import path, include
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/<int:pk>', include('doctor.urls', namespace='schedule'), name='medtests'),
    # path('patient/<int:pk>/medtest/<int:medpk>', views.MedicalTestsDetailView.as_view(), name='medtest_details'),

]