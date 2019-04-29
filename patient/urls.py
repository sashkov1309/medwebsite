from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.index, name='index'),
    # path('patient/<int:pk>/medtest/', views.MedicalTestsView.as_view(), name='medtests'),
    # path('patient/<int:pk>/medtest/<int:medpk>', views.MedicalTestsDetailView.as_view(), name='medtest_details'),

]