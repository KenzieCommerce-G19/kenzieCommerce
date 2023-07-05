from rest_framework import generics
from cart.models import Cart

from cart.serializers import CartSerializer


class CartModifierView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        cart = Cart.objects.get(user=user)
        return cart
