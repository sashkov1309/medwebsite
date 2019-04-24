from django.contrib import admin
from .models import Doctor, Patient, TimeSchedule, MedicalTests

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(TimeSchedule)
admin.site.register(MedicalTests)
