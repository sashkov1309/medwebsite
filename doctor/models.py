from django.db import models

from django.urls import reverse


class Doctor(models.Model):
    GENDER = (
        (0, 'Male'),
        (1, 'Female')
    )
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.BooleanField(choices=GENDER)
    post = models.CharField(max_length=45, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=90, blank=True)
    email = models.CharField(max_length=254, blank=True)
    exam_room = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Patient(models.Model):
    GENDER = (
        (0, 'Male'),
        (1, 'Female')
    )
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    passport_id = models.CharField(max_length=8, default='AA000000')
    gender = models.BooleanField(choices=GENDER)
    birth_date = models.DateField(blank=True)
    address = models.CharField(max_length=90, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=254, blank=True)
    blood_type = models.CharField(max_length=3, blank=True)
    notes = models.TextField(max_length=1000, blank=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('doctor:patient_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.first_name


class TimeSchedule(models.Model):
    day_of_the_week = models.CharField(max_length=15)
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)


class MedicalTests(models.Model):
    READINESS = (
        (0, 'In progress'),
        (1, 'Ready')
    )
    date_application = models.DateTimeField()
    date_registration = models.DateTimeField()
    date_taking_material = models.DateTimeField()
    target_date = models.DateTimeField()
    material = models.CharField(max_length=45)
    diagnosis = models.CharField(max_length=45)
    delivering_method = models.CharField(max_length=25)
    readiness = models.BooleanField(choices=READINESS, default=0)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Test #' + str(self.id) + ' ' + str(self.date_application) + ' (' + str(self.get_readiness_display()) + ')'
