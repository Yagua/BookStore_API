from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("", views.list_all_users, name="user_list"),
    path("register/", views.create_user, name="create_user"),
    path("<int:pk>/", views.UserDetail.as_view(), name="user_detail")
]
