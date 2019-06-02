from django import forms
from doctor.models import *
from django.db import models
from django.forms import ModelForm, DateInput, TextInput, widgets


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'acc_type', 'pat_ref', 'doc_ref']

    def get_initial(self):
        initial_data = super(UserForm, self).get_initial()
        initial_data['doc_ref'] = self.request.user.doc_ref
        return initial_data


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['day', 'time', 'note', 'doctor_id']
        widgets = {
            'day': forms.DateInput(format='%d/%m/%Y',
                                   attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                          'type': 'date'}),

            'note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note for Doctor',
                                           'type': 'text'}),

            'time': widgets.Select(attrs={'class': 'select, form-control'}),
            'doctor_id': widgets.Select(attrs={'class': 'select, form-control'})
        }

    def get_initial(self):
        initial_data = super(ScheduleForm, self).get_initial()
        initial_data['doctor_id'] = self.request.user.doc_ref
        initial_data['patient_id'] = self.request.user.pat_ref
        return initial_data

# apply for visit form
# login
# add patient
# create user account
