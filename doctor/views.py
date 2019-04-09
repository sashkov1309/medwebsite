from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Patient


def index(request):
    return HttpResponse('<h1>index</h1>')


def patient(request):
    all_patients = Patient.objects.all()
    return render(request, 'doctor/index.html', {'all_patients': all_patients, })


def patient_details(request, patient_id):
    try:
        p = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        raise Http404("Patient with this ID doesn't exist.")
    return render(request, 'doctor/patient_details.html', {'p':  p})


def lab(request):
    return HttpResponse('<h1>lab</h1>')


def schedule(request):
    return HttpResponse('<h1>schedule</h1>')
