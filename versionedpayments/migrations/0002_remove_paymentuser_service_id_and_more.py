# Generated by Django 4.1.4 on 2022-12-21 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('versionedpayments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentuser',
            name='service_id',
        ),
        migrations.RemoveField(
            model_name='paymentuser',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='ExpiredPayments',
        ),
        migrations.DeleteModel(
            name='PaymentUser',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
