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
        fields = ['day', 'time', 'note', 'doctor_id', 'patient_id']
        widgets = {
            'day': forms.DateInput(format='%d/%m/%Y',
                                   attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                          'type': 'date'}),

            'note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note for Doctor',
                                           'type': 'text'}),

            'time': widgets.Select(attrs={'class': 'select, form-control'}),
            'doctor_id': widgets.Select(attrs={'class': 'select, form-control'}),
            'patient_id': widgets.HiddenInput(),
        }

    def get_initial(self):
        initial_data = super(ScheduleForm, self).get_initial()
        initial_data['doctor_id'] = self.request.user.doc_ref
        return initial_data


class PatientAddForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name',
                  'middle_name',
                  'last_name',
                  'passport_id',
                  'gender',
                  'birth_date',
                  'address',
                  'phone_number',
                  'email',
                  'blood_type',
                  'notes',
                  'doctor_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name',
                                                 'type': 'text'}),

            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle name',
                                                  'type': 'text'}),

            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name',
                                                'type': 'text'}),
            'passport_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Passport ID',
                                                  'type': 'text'}),
            'gender': widgets.Select(attrs={'class': 'select, form-control'}),
            'birth_date': forms.DateInput(format='%d/%m/%Y',
                                          attrs={'class': 'form-control', 'placeholder': 'Birth date',
                                                 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address',
                                              'type': 'text'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number',
                                                   'type': 'text'}),
            'email': forms.widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email',
                                                     'type': 'text'}),
            'blood_type': widgets.Select(attrs={'class': 'select, form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notes',
                                            'type': 'text'}),
            'doctor_id': widgets.HiddenInput(),
        }


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name',
                  'middle_name',
                  'last_name',
                  'passport_id',
                  'gender',
                  'birth_date',
                  'address',
                  'phone_number',
                  'email',
                  'blood_type',
                  'notes',
                  'doctor_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name',
                                                 'type': 'text'}),

            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle name',
                                                  'type': 'text'}),

            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name',
                                                'type': 'text'}),
            'passport_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Passport ID',
                                                  'type': 'text'}),
            'gender': widgets.Select(attrs={'class': 'select, form-control'}),
            'birth_date': forms.DateInput(format='%d/%m/%Y',
                                          attrs={'class': 'form-control', 'placeholder': 'Birth date',
                                                 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address',
                                              'type': 'text'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number',
                                                   'type': 'text'}),
            'email': forms.widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email',
                                                     'type': 'text'}),
            'blood_type': widgets.Select(attrs={'class': 'select, form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notes',
                                            'type': 'text'}),
            'doctor_id': widgets.HiddenInput(),
        }

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj, created = Patient.objects.get_or_create(col_1=self.kwargs['value_1'], col_2=self.kwargs['value_2'])

        return obj
