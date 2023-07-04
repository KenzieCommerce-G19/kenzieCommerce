from product.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
          "id",
          "name", 
          "quantity", 
          "price", 
          "category", 
          "is_available",
          "user"
        ]
        extra_kwargs = {
          "user": {"read_only": True},
          "is_available":{"default": True}
        }
    def validate(self, attrs):
      quantity = attrs.get("quantity")
      attrs["is_available"] = quantity != 0
      return attrs