from .api import PaymentSet 
from rest_framework import routers 
router = routers.DefaultRouter()#trailing_slash=False
# router.register('api/payments',PaymentSet,'payments')
router.register(r'payments',PaymentSet,'payments')
urlpatterns = router.urls 