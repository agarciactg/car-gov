from django.urls import path

from car.apps.base import views

app_name = "base"

urlpatterns = [
    path("status/", views.status_check, name="status_check"),
]
