from django.urls import path

from car.apps.base.api import views

app_name = "base_api"

urlpatterns = [
    path("api/v1/type_documents/", views.TypeDocumentAPIView.as_view(), name="type_documents"),
    path("api/v1/cities/", views.CityAPIView.as_view(), name="cities"),
    path("api/v1/governments/", views.GovernmentAPIView.as_view(), name="governments"),
]
