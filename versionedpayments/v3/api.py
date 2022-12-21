from payments.models import Payments
from versionedpayments.v3.serializers import PaymentsSerializer
from payments.pagination import StandardResultsSetPagination
from rest_framework import viewsets


class PaymentsViewSetCustomNew(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    pagination_class = StandardResultsSetPagination