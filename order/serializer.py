from order.models import Order
from rest_framework import serializers
from product.serializers import ProductSerializer
from user.models import User
from cart.models import Cart
from exceptions import isNotAvaliableError
from django.shortcuts import get_object_or_404


class OrdeSerializerMany(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "products",
        ]


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    created_orders = serializers.SerializerMethodField()

    def get_created_orders(self, obj):
        filterd_orders = Order.objects.filter(user=obj.user, status="Request_maid")
        order_serialized = OrdeSerializerMany(filterd_orders, many=True)

        return order_serialized.data

    def get_total_price(self, obj):
        filterd_orders = Order.objects.filter(user=obj.user, status="Request_maid")
        for order in filterd_orders:
            initial_price = 0
            for product in order.products.all():
                initial_price = initial_price + product.price
            return initial_price

    class Meta:
        model = Order
        fields = ["total_price", "created_orders"]

    def create(self, validated_data):
        user = validated_data["user"]
        cart = Cart.objects.get(user=user)
        # seller = User.objects.get(id=3)
        products = cart.products.all()

        for product in products:
            if product.quantity == 0:
                raise isNotAvaliableError("product it's not avaliable")

        for product in products:
            product.quantity = product.quantity - 1
            product.save()

        sellers = []

        for product in products:
            sellers.append(product.user)

        print(100 * "=")
        print(sellers)

        no_duplicate_seller = set(sellers)
        seller_list = list(no_duplicate_seller)
        all_products_by_seller = []
        for seller in seller_list:
            for product in products:
                if product.user == seller:
                    all_products_by_seller.append(product)

            order_save = Order.objects.create(user=user, seller=seller)
            order_save.products.set(all_products_by_seller)
            all_products_by_seller.clear()

        return Order.objects.filter(user=user).first()
