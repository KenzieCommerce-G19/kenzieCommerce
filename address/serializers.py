from rest_framework import serializers

from address.models import Address


class AddresseSerializer(serializers.ModelSerializer):
    def update(self, instance: Address, validated_data: dict):
        return super().update(instance, validated_data)

    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "district",
            "city",
            "state",
            "country",
            "zip_code",
        ]
