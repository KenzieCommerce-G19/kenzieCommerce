from django.shortcuts import get_object_or_404
from rest_framework import serializers

from cart.models import Cart
from product.models import Product


class CartSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        print(validated_data)
        product_id = validated_data.get("product_id")
        print(product_id)
        product = get_object_or_404(Product, id=product_id)

        instance.products.add(product)
        return instance

    class Meta:
        model = Cart
        fields = ["id", "user", "products"]
