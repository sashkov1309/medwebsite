# Generated by Django 2.1.1 on 2019-05-26 12:07

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('acc_type', models.IntegerField(choices=[(0, 'Unknown'), (1, 'Doctor'), (2, 'LabAssistant'), (3, 'Patient')], default=0)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('middle_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('gender', models.BooleanField(choices=[(0, 'Male'), (1, 'Female')])),
                ('post', models.CharField(blank=True, max_length=45)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(blank=True, max_length=90)),
                ('email', models.CharField(blank=True, max_length=254)),
                ('exam_room', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_application', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_registration', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_taking_material', models.DateTimeField(default=django.utils.timezone.now)),
                ('target_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('material', models.CharField(max_length=45)),
                ('diagnosis', models.CharField(max_length=45)),
                ('delivering_method', models.CharField(max_length=25)),
                ('readiness', models.BooleanField(choices=[(0, 'In progress'), (1, 'Ready')], default=0)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('middle_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('passport_id', models.CharField(default='AA000000', max_length=8)),
                ('gender', models.BooleanField(choices=[(0, 'Male'), (1, 'Female')])),
                ('birth_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('address', models.CharField(blank=True, max_length=90)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=254)),
                ('blood_type', models.CharField(blank=True, max_length=3)),
                ('notes', models.TextField(blank=True, max_length=1000)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.Doctor')),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='medicaltests',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Patient'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='doc_ref',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pat_ref',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.Patient'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
