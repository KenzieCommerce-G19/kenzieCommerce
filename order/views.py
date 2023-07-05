from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from order.models import Order
from order.serializer import OrderSerializer
from user.permissions import IsSellerAndOwnerOrAdminOrReadOnly


class OrderViews(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerAndOwnerOrAdminOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailsViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerAndOwnerOrAdminOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
