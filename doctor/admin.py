from django.contrib import admin
from .models import Doctor, Patient, TimeSchedule, MedicalTests

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(TimeSchedule)
admin.site.register(MedicalTests)


class EventAdmin(admin.ModelAdmin):
    list_display = ['day_of_the_week', 'start_time', 'end_time', 'doctor_id']
