from order.models import Order
from rest_framework import serializers
from product.serializers import ProductSerializer
from user.models import User


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        initial_price = 0
        for product in obj.products:
            initial_price = initial_price + product.price

    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "user", "seller", "products"]
        extra_kwargs = {
            "products": {"read_only": True},
            "products.quantity": {"write_only": True},
            "user": {"read_only": True},
        }

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
