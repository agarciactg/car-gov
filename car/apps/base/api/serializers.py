from rest_framework import serializers

from car.apps.base.models import City, Government, Province, TypeDocument


class TypeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDocument
        fields = ("id", "initials", "name")


class GovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Government
        fields = ("id", "name", "environmental", "date_created")


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ("id", "name", "date_created")


class CitySerializer(serializers.ModelSerializer):
    government = GovernmentSerializer(many=True)
    province = ProvinceSerializer(many=False)

    class Meta:
        model = City
        fields = ("id", "name", "province", "government", "date_created")


class ExceptionSerializer(serializers.Serializer):
    code_transaction = serializers.ReadOnlyField(
        help_text="Unique error code. Doesn't contain whitespaces. Words are separated by underscores."
    )
    message = serializers.ReadOnlyField(help_text="Human-readable description of the error.")
