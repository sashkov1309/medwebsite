# Generated by Django 2.1.1 on 2019-04-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_medicaltests_readiness'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='passport_id',
            field=models.CharField(default='AA000000', max_length=8),
        ),
    ]
