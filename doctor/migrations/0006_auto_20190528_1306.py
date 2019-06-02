# Generated by Django 2.1.1 on 2019-05-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='note',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.IntegerField(choices=[(0, '9:00 - 9:30'), (1, '9:30 - 10:00'), (2, '10:00 - 10:30'), (3, '10:30 - 11:00'), (4, '11:00 - 11:30'), (5, '11:30 - 12:00'), (6, '12:00 - 12:30'), (7, '12:30 - 13:00'), (8, '13:00 - 13:30'), (9, '13:30 - 14:00'), (10, '14:00 - 14:30'), (11, '14:30 - 15:00'), (12, '15:00 - 15:30'), (13, '15:30 - 16:00'), (14, '16:00 - 16:30'), (15, '16:30 - 17:00'), (16, '17:00 - 17:30'), (17, '17:30 - 18:00')]),
        ),
    ]