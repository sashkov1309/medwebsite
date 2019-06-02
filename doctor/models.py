from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class Doctor(models.Model):
    GENDER = (
        (0, 'Male'),
        (1, 'Female')
    )
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.BooleanField(choices=GENDER, default=0)
    post = models.CharField(max_length=45, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=90, blank=True)
    email = models.CharField(max_length=254, blank=True)
    exam_room = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return 'Doc. ' + self.first_name + ' ' + self.last_name


class Patient(models.Model):
    BLOOD_TYPE = (
        (0, 'O+'),
        (1, 'O-'),
        (2, 'B-'),
        (3, 'B+'),
        (4, 'A-'),
        (5, 'A+'),
        (6, 'AB-'),
        (7, 'AB+')
    )

    GENDER = (
        (0, 'Male'),
        (1, 'Female')
    )
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    passport_id = models.CharField(max_length=8, default='AA000000')
    gender = models.BooleanField(choices=GENDER, default=0)
    birth_date = models.DateField(blank=True, default=timezone.now)
    address = models.CharField(max_length=90, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=254, blank=True)
    blood_type = models.IntegerField(choices=BLOOD_TYPE)
    notes = models.TextField(max_length=1000, blank=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('doctor:patient_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.first_name


class MedicalTests(models.Model):
    READINESS = (
        (0, 'In progress'),
        (1, 'Ready')
    )
    date_application = models.DateTimeField(default=timezone.now)
    date_registration = models.DateTimeField(default=timezone.now)
    date_taking_material = models.DateTimeField(default=timezone.now)
    target_date = models.DateTimeField(default=timezone.now)
    material = models.CharField(max_length=45)
    diagnosis = models.CharField(max_length=45)
    delivering_method = models.CharField(max_length=25)
    readiness = models.BooleanField(choices=READINESS, default=0)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('doctor:medtest_details', kwargs={'pk': self.patient_id.pk, 'medpk': self.pk})

    def __str__(self):
        return 'Test #' + str(self.id) + ' ' + str(self.date_application) + ' (' + str(
            self.get_readiness_display()) + ')'


class UserProfile(AbstractBaseUser, PermissionsMixin):
    accType = (
        (0, 'Unknown'),
        (1, 'Doctor'),
        (2, 'LabAssistant'),
        (3, 'Patient'),
        (4, 'Admin'),
    )
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    acc_type = models.IntegerField(choices=accType, default=0)
    pat_ref = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    doc_ref = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = "username"
    objects = UserManager()
    REQUIRED_FIELDS = ["email"]


class Schedule(models.Model):
    AVAILABLE_TIME = (
        (0, '9:00 - 9:30'),
        (1, '9:30 - 10:00'),
        (2, '10:00 - 10:30'),
        (3, '10:30 - 11:00'),
        (4, '11:00 - 11:30'),
        (5, '11:30 - 12:00'),
        (6, '12:00 - 12:30'),
        (7, '12:30 - 13:00'),
        (8, '13:00 - 13:30'),
        (9, '13:30 - 14:00'),
        (10, '14:00 - 14:30'),
        (11, '14:30 - 15:00'),
        (12, '15:00 - 15:30'),
        (13, '15:30 - 16:00'),
        (14, '16:00 - 16:30'),
        (15, '16:30 - 17:00'),
        (16, '17:00 - 17:30'),
        (17, '17:30 - 18:00'),
    )
    day = models.DateField()
    time = models.IntegerField(choices=AVAILABLE_TIME)
    note = models.CharField(blank=True, null=True, max_length=50)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.day) + ' - (' + str(self.get_time_display()) + ') ' + str(self.patient_id)

    def get_absolute_url(self):
        return reverse('main:index')
