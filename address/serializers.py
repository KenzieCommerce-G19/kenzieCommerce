from rest_framework import serializers

from address.models import Address


class AddresseSerializer(serializers.ModelSerializer):
    def create(self, validate_data):
        return Address.objects.create(**validate_data)

    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "districk",
            "city",
            "state",
            "country",
            "zip_code",
        ]
