from .models import UserProfile
from django import forms
from doctor.models import Patient
from django.db import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'acc_type', 'pat_ref', 'doc_ref']

    def get_initial(self):
        initial_data = super(UserForm, self).get_initial()
        initial_data['doc_ref'] = self.request.user.doc_ref
        return initial_data
