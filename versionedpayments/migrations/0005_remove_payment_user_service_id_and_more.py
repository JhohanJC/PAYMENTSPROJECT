# Generated by Django 4.1.4 on 2022-12-21 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('versionedpayments', '0004_payment_user_services_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_user',
            name='service_id',
        ),
        migrations.RemoveField(
            model_name='payment_user',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Expired_payments',
        ),
        migrations.DeleteModel(
            name='Payment_user',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
