from rest_framework.generics import ListAPIView

from car.apps.base.api.serializers import CitySerializer, TypeDocumentSerializer
from car.apps.base.models import City, TypeDocument
from car.apps.base.utils import StandardResultsPagination
from car.utils.mixins import APIBasePermissionsMixin


# Api of  City
class CityAPIView(APIBasePermissionsMixin, ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.activos()
    pagination_class = StandardResultsPagination


# Api of  Type Documents
class TypeDocumentAPIView(APIBasePermissionsMixin, ListAPIView):
    serializer_class = TypeDocumentSerializer
    queryset = TypeDocument.objects.activos()
    pagination_class = StandardResultsPagination
