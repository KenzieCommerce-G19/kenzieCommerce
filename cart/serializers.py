from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelField):
    def update(self, instance: Cart, validate_data) -> Cart:
        instance.save()

        return instance

    class Meta:
        model = Cart
        fields = ["id", "user_id", "products"]
