# Generated by Django 2.1.1 on 2019-04-28 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_patient_passport_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicaltests',
            name='doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.Doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.Doctor'),
        ),
        migrations.AlterField(
            model_name='timeschedule',
            name='doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.Doctor'),
        ),
    ]
