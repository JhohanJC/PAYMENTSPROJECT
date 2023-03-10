# Generated by Django 4.1.4 on 2022-12-18 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('NF', 'Netflix'), ('AP', 'Amazon Video'), ('ST', 'Strat +'), ('PM', 'Paramount +')], default='NF', max_length=2)),
                ('date_payment', models.DateField(auto_now_add=True)),
                ('amount', models.FloatField(default=0.0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.user')),
            ],
        ),
    ]
