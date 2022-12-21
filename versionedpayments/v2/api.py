from payments.models import Payments
from users.models import User
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from versionedpayments.base.models import (Services,Payment_user,Expired_payments)
from versionedpayments.v2.serializers import (ServicesSerializer, PaymentUserSerializer,
ExpiredPaymentsSerializer,UsersSerializer)
from payments.pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
class ServicesViewSetCustomNew(viewsets.ModelViewSet):
    queryset = Services.objects.get_queryset().order_by('id')
    serializer_class = ServicesSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'others'

class PaymentUserViewSetCustomNew(viewsets.ModelViewSet):
    queryset = Payment_user.objects.get_queryset().order_by('id')
    serializer_class = PaymentUserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    # Definición de la clave
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'others'
class ExpiredPaymentsViewSetCustomNew(viewsets.ModelViewSet):
    queryset = Expired_payments.objects.get_queryset().order_by('id')
    serializer_class = ExpiredPaymentsSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    # Definición de la clave
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'others'

# Version 1

class UsersViewSetCustomNew(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    # Definición de la clave
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'others'