from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.BooleanField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Patient(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.BooleanField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
