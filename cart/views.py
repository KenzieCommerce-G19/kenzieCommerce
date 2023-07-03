from rest_framework import generics

from cart.models import Cart
from cart.serializers import CartSerializer
from user.permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated


class CartView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
