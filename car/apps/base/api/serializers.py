from rest_framework import serializers

from car.apps.base.models import City, TypeDocument


class TypeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDocument
        fields = ("id", "initials", "name")


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "date_created")


class ExceptionSerializer(serializers.Serializer):
    code_transaction = serializers.ReadOnlyField(
        help_text="Unique error code. Doesn't contain whitespaces. Words are separated by underscores."
    )
    message = serializers.ReadOnlyField(help_text="Human-readable description of the error.")