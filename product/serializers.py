from product.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    is_available = serializers.SerializerMethodField()

    def get_is_available(self, obj):
        return obj.quantity > 0

    class Meta:
        model = Product
        fields = [
          "id", 
          "name", 
          "quantity", 
          "price", 
          "category", 
          "is_available", 
          "user"]
        extra_kwargs = {
            "user": {"read_only": True},
        }
