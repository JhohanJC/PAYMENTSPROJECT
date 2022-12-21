from rest_framework import routers
from payments.api import PaymentSet as PaymentsCustomV1
from versionedpayments.v2.api import UsersViewSetCustomNew as UsersCustomV1
from versionedpayments.v2.api import ServicesViewSetCustomNew as ServicesCustomV2
from versionedpayments.v2.api import PaymentUserViewSetCustomNew as PaymentUserCustomV2
from versionedpayments.v2.api import ExpiredPaymentsViewSetCustomNew as ExpiredPaymentsCustomV2
from django.urls import path
# from users.views import SignUpView, LoginView
# ...
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )
router = routers.DefaultRouter()#trailing_slash=False
router.register(r'payments', PaymentsCustomV1, 'payments')
router.register(r'users', UsersCustomV1, 'users')
router.register(r'services', ServicesCustomV2, 'services')
router.register(r'payment_user', PaymentUserCustomV2, 'payment_user')
router.register(r'expired_payments', ExpiredPaymentsCustomV2, 'expired_payments')


# urlpatterns = [
#     #...
#     path("signup/", SignUpView.as_view(), name="signup"),
#     path("login/", LoginView.as_view(), name="login"),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
#     #...
# ]

urlpatterns = router.urls