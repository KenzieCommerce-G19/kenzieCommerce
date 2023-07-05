from order.models import Order
from rest_framework import serializers
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "price", "user", "products"]
        extra_kwargs = {"products": {"read_only": True}}

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
