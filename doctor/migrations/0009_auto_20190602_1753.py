# Generated by Django 2.1.1 on 2019-06-02 14:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_auto_20190528_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicaltests',
            name='date_application',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='medicaltests',
            name='date_registration',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='medicaltests',
            name='date_taking_material',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='medicaltests',
            name='target_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
