from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import SendOTPView, VerifyOTPView


urlpatterns = [
    #path('register/', RegisterView.as_view(), name = 'register'),

    path('send_OTP/', SendOTPView.as_view(), name='send_code'),
    path('Verify_OTP/', VerifyOTPView.as_view(), name='Verify_code'),

    path('users/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
]
