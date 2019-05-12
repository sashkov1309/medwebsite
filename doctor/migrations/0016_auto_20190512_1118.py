# Generated by Django 2.1.1 on 2019-05-12 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0015_auto_20190512_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeschedule',
            name='title',
        ),
        migrations.AddField(
            model_name='timeschedule',
            name='patient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.Patient'),
        ),
    ]
