from order.models import Order
from rest_framework import serializers
from product.serializers import ProductSerializer
from user.models import User
from cart.models import Cart
from exceptions import isNotAvaliableError
from django.shortcuts import get_object_or_404


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    total_price = serializers.SerializerMethodField()

    # def quantity_check(self, obj):
    #     user = get_object_or_404(User, id=self.request.data["user_id"])
    #     cart = Cart.objects.get(user=user)

    #     products = cart.products.all()

    #     print("texxxxtooooooo", products)
    #     for product in obj.products.all():
    #         if product.quantity == 0:
    #             raise isNotAvaliableError("product it's not avaliable")

    def get_total_price(self, obj):
        ...

    #     if obj.products:
    #         initial_price = 0
    #         for product in obj.products.all():
    #             initial_price = initial_price + product.price

    # def new_quantity(self, obj):
    #     new_quantity = 0
    #     for product in obj.products.all():
    #         new_quantity = product.quantity - 1

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "created_at",
            "total_price",
            "user",
            "products",
            "seller",
        ]
        extra_kwargs = {
            "products": {"read_only": True},
            "products.quantity": {"write_only": True},
            "user": {"read_only": True},
            "seller": {"read_only": True},
        }

    def create(self, validated_data):
        # self.quantity_check(validated_data)
        # self.new_quantity(validated_data)
        return Order.objects.create(**validated_data)
