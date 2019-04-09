from django.db import models


class Doctor(models.Model):
    doctorFirstName = models.CharField(max_length=100)
    doctorMiddleName = models.CharField(max_length=100)
    doctorLastName = models.CharField(max_length=100)
    Gender = models.BooleanField()

    def __str__(self):
        return self.doctorFirstName + ' ' + self.doctorLastName


class Patient(models.Model):
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patientFirstName = models.CharField(max_length=100)
    patientMiddleName = models.CharField(max_length=100)
    patientLastName = models.CharField(max_length=100)
    Gender = models.BooleanField()

    def __str__(self):
        return self.patientFirstName + ' ' + self.patientLastName
