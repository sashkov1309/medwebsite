from django.urls import path
from . import views
from doctor.views import medtests_update_form_view
app_name = 'lab'

urlpatterns = [
    path('', views.index, name='index'),
    path('tests/', views.MedicalTestsView.as_view(), name='medtests'),
    path('todo/', views.MedicalTestsTODOView.as_view(), name='medtests_todo'),
    path('<int:pk>', medtests_update_form_view, name='medtests_update'),
    path('tests/<int:medpk>', views.MedicalTestsDetailView.as_view(),    name='medtest_details')
]
