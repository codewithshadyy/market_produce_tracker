from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

from .views import UserRegistrationView

urlpatterns = [
    path("auth/register/", UserRegistrationView.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view()),
    path("auth/refresh", TokenRefreshView.as_view()),
]
