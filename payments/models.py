from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Payments(models.Model):
    class Services(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Star +')
        PARAMOUNT = 'PM', _('Paramount +')
    service = models.CharField(
        max_length=2, 
        choices = Services.choices, 
        default = Services.NETFLIX,
    )
    date_payment = models.DateField(auto_now_add=True)# fecha de pago
    amount = models.FloatField(default=0.0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    # #id v
    # #name v
    # #descripcion
    # description = models.TextField()
    # #logo
    # logo = models.ImageField(upload_to='uploads/')