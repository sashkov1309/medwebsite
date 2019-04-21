from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Patient, MedicalTests


def index(request):
    return HttpResponse('<h1>doctor</h1>')


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
