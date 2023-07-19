from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from car.apps.base import models as base_models
from car.apps.users.models import User


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)  # comment out if you don't want this
        data["access"] = str(refresh.access_token)
        # data["type_user"] = self.user.get_type_user_display()

        return data


class UserSerializer(serializers.ModelSerializer):
    type_user = serializers.CharField(source="get_type_user_display")

    class Meta:
        model = User
        fields = (
            "id",
            "uuid",
            "type_user",
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "avatar",
        )


class SerializerTokenAuth(serializers.Serializer):
    refresh = serializers.CharField(required=True)
    access = serializers.CharField(required=True)
    # type_user = serializers.CharField(required=False)


class UserCreateSerializer(serializers.Serializer):
    """
    Serializer to create user
    """

    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True)
    type_user = serializers.ChoiceField(
        write_only=True,
        required=True,
        choices=User.UserType.choices,
    )
    email = serializers.CharField(write_only=True, required=False, allow_blank=True, default="")
    phone = serializers.CharField(write_only=True, allow_null=True, required=False)
    city = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=base_models.City.objects.filter(status=base_models.BaseModel.Status.ACTIVE),
        allow_null=True,
        required=False,
    )
    is_email_verified = serializers.BooleanField(write_only=True, required=False, default=False)
    verification_code = serializers.CharField(write_only=True, required=False, allow_null=True)

    def create(self, validated_data):
        with atomic():
            user_data = {
                "username": validated_data.pop("username"),
                "first_name": validated_data.pop("first_name"),
                "last_name": validated_data.pop("last_name"),
                "type_user": validated_data.pop("type_user"),
                "email": validated_data.pop("email"),
                "phone": validated_data.get("phone", None),
                "city": validated_data.get("city", None),
                "avatar": validated_data.pop("avatar", None),
            }

            # Save the information of the user
            user = User.objects.create(**user_data)
            user.set_password(str(validated_data.pop("password")))
            user.save()

        return user


class UserDetailSerializer(serializers.ModelSerializer):
    type_user = serializers.CharField(source="get_type_user_display")

    class Meta:
        model = User
        fields = (
            "id",
            "type_user",
            "first_name",
            "last_name",
            "username",
            "avatar",
            "is_active",
        )
