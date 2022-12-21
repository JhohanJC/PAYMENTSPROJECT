from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payments  
from .serializers import PaymentSerializer
from .pagination import StandardResultsSetPagination
from rest_framework.throttling import UserRateThrottle
class PaymentSet(viewsets.ModelViewSet):
    queryset = Payments.objects.get_queryset().order_by('id')
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filter_backends = [filters.SearchFilter]
    # permission_classes = [permissions.AllowAny]
    permission_classes = [IsAuthenticated]
    search_fields = ['user_id', 'date_payment', 'service']
    throttle_classes = 'payments'