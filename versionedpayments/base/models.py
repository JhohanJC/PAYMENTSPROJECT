from django.db import models

# Create your models here.
from payments.models import Payments 
from payments.models import User 
from django.utils.translation import gettext_lazy as _
class Services(models.Model):
    class Name(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Star +')
        PARAMOUNT = 'PM', _('Paramount +')
    name = models.CharField(max_length=2, 
    choices = Name.choices, 
    default = Name.NETFLIX,)
    Description = models.TextField()
    logo = models.ImageField(upload_to='img/')
class Payment_user(models.Model):
    # id_paymentuser = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    paymet_date = models.DateField(auto_now=True)
    expiracion_date = models.DateTimeField(auto_now_add=True)
class Expired_payments(models.Model):
    # id_exp_payments = models.AutoField(primary_key=True)
    payment_user_id = models.ForeignKey(Payment_user, on_delete=models.CASCADE)
    penalty_fee_amount = models.FloatField(default=0.0)
