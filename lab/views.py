from doctor.models import Patient, MedicalTests
from django.views.generic.edit import UpdateView
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    return render(request, 'lab/index.html', {})


class MedicalTestsUpdate(UpdateView):
    model = MedicalTests
    fields = ['date_application', 'diagnosis', 'readiness']


class MedicalTestsView(generic.ListView):
    template_name = 'doctor/medtest.html'

    def get_queryset(self):
        try:
            my_model = MedicalTests.objects.filter(readiness=True)
        except:
            raise Http404
        return my_model


class MedicalTestsTODOView(generic.ListView):
    template_name = 'doctor/medtest.html'

    def get_queryset(self):
        try:
            my_model = MedicalTests.objects.filter(readiness=False)
        except:
            raise Http404
        return my_model


class MedicalTestsDetailView(generic.DetailView):
    model = MedicalTests
    template_name = 'doctor/medtest_details.html'
    queryset = Patient.objects.all()

    def get_object(self, queryset=None):
        m_id = self.kwargs.get("medpk")
        return get_object_or_404(MedicalTests, id=m_id)
