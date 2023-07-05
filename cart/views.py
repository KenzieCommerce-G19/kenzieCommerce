from rest_framework import generics

from cart.models import Cart
from cart.serializers import CartSerializer
from user.permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated


class CartModifaierView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
