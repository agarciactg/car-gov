from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenViewBase

from car.apps.base.api import serializers as base_serializer
from car.apps.base.utils import StandardResultsPagination
from car.apps.users import exceptions as user_exceptions
from car.apps.users.api import serializers
from car.utils import mixins


class TokenObtainPairView(mixins.APIWithCustomerPermissionsMixin, TokenViewBase):
    """
    Return JWT tokens (access and refresh) for specific user based on username and password.
    """

    serializer_class = serializers.UserTokenObtainPairSerializer

    @swagger_auto_schema(
        operation_description="Endpoint para obtener un token.",
        request_body=base_serializer.ExceptionSerializer(many=False),
        responses={
            200: serializers.SerializerTokenAuth(many=True),
            401: openapi.Response(
                type=openapi.TYPE_OBJECT,
                description="No tiene Autorización.",
                schema=base_serializer.ExceptionSerializer(many=False),
                examples={
                    "application/json": user_exceptions.UserUnauthorizedAPIException().get_full_details()
                },
            ),
            404: openapi.Response(
                type=openapi.TYPE_OBJECT,
                description="No tiene registro del Usuario.",
                schema=base_serializer.ExceptionSerializer(many=False),
                examples={
                    "application/json": user_exceptions.UserDoesNotExistsAPIException().get_full_details()
                },
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenRefreshView(mixins.APIWithCustomerPermissionsMixin, TokenViewBase):
    """
    Renew tokens (access and refresh) with new expire time based on specific user's access token.
    """

    serializer_class = TokenRefreshSerializer


class UserCreateAPIView(mixins.APIWithCustomerPermissionsMixin, generics.ListAPIView):
    """
    Endpoint to create a user
    """

    pagination_class = StandardResultsPagination
    serializer_class = serializers.UserCreateSerializer

    @swagger_auto_schema(
        operation_description="Endpoint para crear un usuario.",
        request_body=base_serializer.ExceptionSerializer(many=False),
        responses={
            200: serializers.UserCreateSerializer(many=True),
            401: openapi.Response(
                type=openapi.TYPE_OBJECT,
                description="No tiene Autorización.",
                schema=base_serializer.ExceptionSerializer(many=False),
                examples={
                    "application/json": user_exceptions.UserUnauthorizedAPIException().get_full_details()
                },
            ),
            404: openapi.Response(
                type=openapi.TYPE_OBJECT,
                description="No tiene registro del Usuario.",
                schema=base_serializer.ExceptionSerializer(many=False),
                examples={
                    "application/json": user_exceptions.UserDoesNotExistsAPIException().get_full_details()
                },
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = serializers.UserCreateSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        detail = serializers.UserDetailSerializer(user, many=False)
        return Response(detail.data)
