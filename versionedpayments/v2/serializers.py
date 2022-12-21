from rest_framework import serializers
# from payments.models import Payments
from versionedpayments.base.models import Services, Payment_user, Expired_payments
from users.models import User
# version 1
# class PaymentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payments
#         fields = '__all__'
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username"]
# version 2   
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'
class ExpiredPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = '__all__'