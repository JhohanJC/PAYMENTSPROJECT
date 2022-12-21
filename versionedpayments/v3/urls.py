from rest_framework import (routers)
from versionedpayments.v3.api import PaymentsViewSetCustomNew as PaymentsCustomV3

router = routers.DefaultRouter(trailing_slash=False)

router.register('payments', PaymentsCustomV3, 'payments')

urlpatterns = router.urls
