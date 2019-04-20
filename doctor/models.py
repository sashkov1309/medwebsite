from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.BooleanField()
    post = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=15)
    adress = models.CharField(max_length=90)
    email = models.CharField(max_length=255)
    exam_room = models.CharField(max_length=6)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Patient(models.Model):
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.BooleanField()
    birth_date = models.DateField()
    adress = models.CharField(max_length=90)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=3)
    notes = models.TextField(max_length=1000)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class TimeScedule(models.Model):
    day_of_the_week = models.CharField(max_length=15)
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class MeedicalTests(models.Model):
    date_application = models.DateTimeField()
    date_registration = models.DateTimeField()
    date_taking_material = models.DateTimeField()
    target_date = models.DateTimeField()
    material = models.CharField(max_length=45)
    diagnosis = models.CharField(max_length=45)
    delivering_method = models.CharField(max_length=25)
    patinet_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
