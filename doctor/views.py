from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, MedicalTests, TimeSchedule
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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


class PatientCreate(CreateView):
    model = Patient
    fields = ['first_name', 'first_name', 'last_name', 'gender', 'birth_date', 'address', 'phone_number', 'email',
              'blood_type', 'notes', 'doctor_id']


class MedicalTestCreate(CreateView):
    model = MedicalTests
    fields = ['date_application', 'date_registration', 'date_taking_material', 'target_date', 'material',
              'delivering_method', 'patient_id', 'doctor_id']


class PatientUpdate(UpdateView):
    model = Patient
    fields = ['first_name', 'first_name', 'last_name', 'gender', 'birth_date', 'address', 'phone_number', 'email',
              'blood_type', 'notes', 'doctor_id']


class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('doctor:index')


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


class UserFormView(View):
    form_class = UserForm
    template_name = 'main/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # cleaned (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
