# Generated by Django 4.1.4 on 2022-12-21 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('versionedpayments', '0005_remove_payment_user_service_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('NF', 'Netflix'), ('AP', 'Amazon Video'), ('ST', 'Star +'), ('PM', 'Paramount +')], default='NF', max_length=2)),
                ('Description', models.TextField()),
                ('logo', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('paymet_date', models.DateField(auto_now=True)),
                ('expiracion_date', models.DateTimeField(auto_now_add=True)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versionedpayments.services')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expired_payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_fee_amount', models.FloatField(default=0.0)),
                ('payment_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versionedpayments.payment_user')),
            ],
        ),
    ]
