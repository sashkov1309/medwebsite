from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Patient, MedicalTests, TimeSchedule
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'doctor/index.html'

    def get_queryset(self):
        return Patient.objects.all()


class PatientsView(generic.ListView):
    template_name = 'doctor/patient.html'

    def get_queryset(self):
        return Patient.objects.all()


class PatientDetailView(generic.DetailView):
    model = Patient
    template_name = 'doctor/patient_details.html'
    queryset = Patient.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Patient, id=id_)


class ScheduleView(generic.DetailView):
    model = Patient
    template_name = 'doctor/schedule.html'
    queryset = TimeSchedule.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(TimeSchedule, doctor_id=id_)


class MedicalTestsView(generic.ListView):
    template_name = 'doctor/medtest.html'

    def get_queryset(self):
        return MedicalTests.objects.filter(patient_id=self.kwargs.get("pk"))


class MedicalTestsDetailView(generic.DetailView):
    model = MedicalTests
    template_name = 'doctor/medtest_details.html'
    queryset = Patient.objects.all()

    def get_object(self, queryset=None):
        p_id_ = self.kwargs.get("pk")
        m_id_ = self.kwargs.get("medpk")
        return get_object_or_404(MedicalTests, id=m_id_, patient_id=p_id_)
