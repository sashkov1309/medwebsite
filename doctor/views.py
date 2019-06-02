from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, MedicalTests, Schedule
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import datetime, date, time, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
import dateutil.parser
from datetime import datetime
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .forms import ScheduleForm


# from django.forms.extras.widgets import SelectDateWidget

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


class ApplyForVisitView(CreateView):
    model = Schedule
    fields = ['day', 'time', 'note', 'doctor_id', 'patient_id']

    def get_initial(self):
        initial_data = super(ApplyForVisitView, self).get_initial()
        initial_data['patient_id'] = self.request.user.pat_ref
        initial_data['doctor_id'] = self.request.user.doc_ref
        initial_data['day'] = date.today()
        return initial_data

    # def get_form(self):
    #     form = super(ApplyForVisitView, self).get_form()
    #     form.fields['day'].widget = forms.SelectDateWidget()
    #     return form


class WeekView(generic.ListView):
    model = Schedule
    template_name = 'doctor/week.html'

    def get_context_data(self, **kwargs):
        fin = {}
        d_id = Doctor.objects.get(pk=self.kwargs.get("pk"))
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        allowed_users = [1, 4]

        curr_date = datetime.today()
        start_week = curr_date - timedelta(curr_date.weekday())
        end_week = start_week + timedelta(6)

        objects = Schedule.objects.filter(doctor_id=d_id, day__range=[start_week, end_week])
        context = '<ul class="list-group">'
        context += '<li class="list-group-item"><b>Doctor: </b>' + str(self.request.user.doc_ref)
        context += '<li class="list-group-item"><b>'
        context += str(start_week.date()) + ' (' + str(days[start_week.weekday()]) + ') - '
        context += str(end_week.date()) + ' (' + str(days[end_week.weekday()]) + ')</b>'
        context += '<i> Current date: ' + str(curr_date.date()) + ' (' + str(days[curr_date.weekday()]) + ')</i></li>'

        for i in range(days.__len__() - 2):
            curr_day_month = start_week + timedelta(i)
            context += '<li class="list-group-item" style="font-size: 150%"><b>' + days[i] + '</b> ' + str(
                curr_day_month.day)
            if i == curr_date.weekday():
                context += ' <i>(Today)</i>'
            context += '</li>'
            for obj in objects:
                if i == obj.day.weekday():
                    item = '<li class="list-group-item">'
                    item += str(obj.get_time_display())

                    if self.request.user.acc_type in allowed_users:
                        item += ' <b>Patient:</b> ' + str(obj.patient_id)
                        item += ' <b>Note:</b> ' + str(obj.note) + '</i>'
                    else:
                        item += '<div class="booked"><i> Booked</i></div>'
                    item += '</li>'
                    context += item
            if i != 4:
                context += '<li class="list-group-item"></li>'
        context += '</ul>'
        fin['week'] = mark_safe(context)
        return fin


class UserFormView(View):
    form_class = UserForm
    template_name = 'doctor/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=True)
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            #
            # user.set_password(password)
            # user.save()
            #
            # user = authenticate(username=username, password=password)
            #
            # if user is not None:
            #     if user.is_active:
            #         login(request, user)

        return render(request, 'doctor/index.html')


def schedule_view(request):
    form = ScheduleForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'doctor/forms/patient_schedule_form.html', context)
