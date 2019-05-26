from django.contrib.auth.models import User
from django import forms
from doctor.models import Patient
from django.db import models


class UserForm(forms.ModelForm):
    TYPES = (
        (0, 'Patient'),
        (1, 'Doctor'),
        (2, 'Lab')
    )
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
