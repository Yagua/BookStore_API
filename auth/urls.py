from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, LogOutView

app_name = "auth"

urlpatterns = [
    path("login/", LoginView.as_view(), name="system_login"),
    path("logout/", LogOutView.as_view(), name="system_logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
