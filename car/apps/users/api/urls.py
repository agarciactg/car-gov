from django.urls import path

from car.apps.users.api import views

app_name = "user_api"

urlpatterns = [
    path("api/v1/auth/token/", views.TokenObtainPairView.as_view(), name="token"),
    path("api/v1/auth/token/refresh/", views.TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/user/create/", views.UserCreateAPIView.as_view(), name="user_create"),
]
