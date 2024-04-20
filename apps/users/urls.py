from django.urls import path
from .views import *
# (
#     UserRegistrationView, 
#     UserAuthenticationView, 
#     EmailVerificationView, 
#     PasswordResetView, 
#     UserProfileView
# )

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserAuthenticationView.as_view(), name='user-login'),
    path('verify-email/', EmailVerificationView.as_view(), name='email-verify'),
    path('reset-password/', PasswordResetView.as_view(), name='password-reset'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]



























# from django.urls import path
# from .views import UserRegistrationView, UserAuthenticationView, EmailVerificationView, PasswordResetView, UserProfileView

# urlpatterns = [
#     path('register/', UserRegistrationView.as_view(), name='user-register'),
#     path('login/', UserAuthenticationView.as_view(), name='user-login'),
#     path('verify-email/', EmailVerificationView.as_view(), name='email-verify'),
#     path('reset-password/', PasswordResetView.as_view(), name='password-reset'),
#     path('profile/', UserProfileView.as_view(), name='user-profile'),
# ]
