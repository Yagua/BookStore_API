from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from user.views import RestartUserPasswordView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("library.urls")),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/auth/login/", include("auth.urls")),
    path("api/v1/carts/", include("cart.urls")),
    path("api/v1/profile/", include("user_profile.urls")),
    path("api/v1/search/", include("search.urls")),
    path(
        "password/reset/confirm/<str:uid>/<str:token>/",
        RestartUserPasswordView.as_view(),
        name="reset_password",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
