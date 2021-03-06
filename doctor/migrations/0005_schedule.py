# Generated by Django 2.1.1 on 2019-05-26 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20190526_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('time', models.IntegerField(choices=[(0, '9:00'), (1, '9:30'), (2, '10:00'), (3, '10:30'), (4, '11:00'), (5, '11:30'), (6, '12:00'), (7, '12:30'), (8, '13:00'), (9, '13:30'), (10, '14:00'), (11, '14:30'), (12, '15:00'), (13, '15:30'), (14, '16:00'), (15, '16:30'), (16, '17:00'), (17, '17:30')])),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Patient')),
            ],
        ),
    ]
