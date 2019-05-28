from django.contrib import admin
from .models import Doctor, Patient, TimeSchedule, MedicalTests, UserProfile, Schedule
from django.contrib import admin

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(TimeSchedule)
admin.site.register(Schedule)
admin.site.register(MedicalTests)
admin.site.register(UserProfile)
