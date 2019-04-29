from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('info/', views.info, name='info'),
    # path('patient/<int:patient_id>', views.patient_details, name='patient_details'),
]
