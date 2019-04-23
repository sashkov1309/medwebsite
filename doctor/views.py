from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Patient, MedicalTests
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'doctor/index.html'

    def get_queryset(self):
        return Patient.objects.all()


class DetailView(generic.DetailView):
    model = Patient
    template_name = 'doctor/patient_details.html'


def index(request):
    return render(request, 'doctor/index.html', {})


def patient(request):
    all_patients = Patient.objects.all()
    return render(request, 'doctor/index.html', {'all_patients': all_patients, })


def patient_details(request, patient_id):
    patients = get_object_or_404(Patient, id=patient_id)
    return render(request, 'doctor/patient_details.html', {'patients': patients})


def medtest_details(request, patient_id, medtest_id):
    patients = get_object_or_404(Patient, id=patient_id)
    medtests = get_object_or_404(MedicalTests, id=patient_id)
    return render(request, 'doctor/patient_details.html', {'patients': patients,
                                                           'medtests': medtests})


def lab(request):
    return HttpResponse('<h1>lab</h1>')


def schedule(request):
    return HttpResponse('<h1>schedule</h1>')
