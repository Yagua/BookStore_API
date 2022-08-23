from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.get_user_profile, name="user_profile"),
    path("update/", views.update_user_profile, name="update_user_profile")
]
