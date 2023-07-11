from rest_framework import serializers

from cart.models import Cart
from product.models import Product
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = ["id", "user", "products"]
        extra_kwargs = {"products": {"read_only": True}}

    def update(self, instance, validated_data):
        products_data = validated_data.get("products", [])
        for product_id in products_data:
            products = Product.objects.filter(**product_id)
            for product in products:
                instance.products.add(product)
        return instance
