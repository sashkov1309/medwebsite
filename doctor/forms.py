from django import forms
from doctor.models import *
from django.db import models
from django.forms import ModelForm, DateInput, TextInput, widgets


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username',
                  'email',
                  'password',
                  'acc_type',
                  'pat_ref',
                  'doc_ref']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',
                                               'type': 'text'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email',
                                             'type': 'text'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                   'type': 'password'}),
            'acc_type': widgets.Select(attrs={'class': 'select, form-control'}),
            'pat_ref': widgets.Select(attrs={'class': 'select, form-control'}),
            'doc_ref': widgets.Select(attrs={'class': 'select, form-control'}),
        }

    def get_initial(self):
        initial_data = super(UserForm, self).get_initial()
        initial_data['doc_ref'] = self.request.user.doc_ref
        return initial_data


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['day', 'time', 'note', 'doctor_id', 'patient_id']
        widgets = {
            'day': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date',
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


class PatientForm(forms.ModelForm):
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
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Birth date',
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


class MedicalTestsForm(forms.ModelForm):
    class Meta:
        model = MedicalTests
        fields = ['date_application',
                  'date_registration',
                  'date_taking_material',
                  'target_date',
                  'material',
                  'diagnosis',
                  'delivering_method',
                  'readiness',
                  'patient_id',
                  'doctor_id']
        widgets = {
            'date_application': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_registration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_taking_material': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'target_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material', 'type': 'text'}),
            'diagnosis': forms.Textarea(attrs={'size': 10, 'class': 'form-control', 'placeholder': 'Result', 'type': 'text'}),
            'delivering_method': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Delivering Method',
                                                        'type': 'text'}),
            'readiness': widgets.Select(attrs={'class': 'select, form-control'}),
            'patient_id': widgets.HiddenInput(),
            'doctor_id': widgets.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MedicalTestsForm, self).__init__(*args, **kwargs)
        self.fields['diagnosis'].label = "Test Result"
        if self.request.user.acc_type == 2:  # lab
            self.fields['date_application'].widget.attrs['readonly'] = True
            self.fields['material'].widget.attrs['readonly'] = True
            self.fields['readiness'].widget.attrs['readonly'] = True
            self.fields['patient_id'].widget.attrs['readonly'] = True
            self.fields['doctor_id'].widget.attrs['readonly'] = True
        else:  # doc
            self.fields['date_registration'].widget.attrs['readonly'] = True
            self.fields['date_taking_material'].widget.attrs['readonly'] = True
            self.fields['target_date'].widget.attrs['readonly'] = True
            self.fields['readiness'].widget.attrs['readonly'] = True
            # self.fields['readiness'].widget.attrs['disabled'] = True
            self.fields['patient_id'].widget.attrs['readonly'] = True
            self.fields['doctor_id'].widget.attrs['readonly'] = True
            self.fields['diagnosis'].widget.attrs['readonly'] = True
            self.fields['diagnosis'].required = False
