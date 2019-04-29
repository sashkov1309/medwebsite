from django.urls import path
from . import views

app_name = 'lab'

urlpatterns = [
    path('', views.index, name='index'),
    path('tests/', views.MedicalTestsView.as_view(), name='medtests'),
    path('todo/', views.MedicalTestsTODOView.as_view(), name='medtests_todo'),
    path('<int:pk>', views.MedicalTestsUpdate.as_view(), name='medtests_update'),
    path('tests/<int:medpk>', views.MedicalTestsDetailView.as_view(),    name='medtest_details')
]
