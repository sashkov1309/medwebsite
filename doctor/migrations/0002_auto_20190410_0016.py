# Generated by Django 2.1.1 on 2019-04-09 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='doctorFirstName',
            new_name='doctor_first_name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='doctorLastName',
            new_name='doctor_last_name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='doctorMiddleName',
            new_name='doctor_middle_name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='patientFirstName',
            new_name='patient_first_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='patientLastName',
            new_name='patient_last_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='patientMiddleName',
            new_name='patient_middle_name',
        ),
    ]