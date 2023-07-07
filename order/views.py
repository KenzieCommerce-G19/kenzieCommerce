from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from order.models import Order
from user.models import User
from order.serializer import OrderSerializer
from user.permissions import IsSellerAndOwnerOrAdmin, IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated


class OrderViews(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(
            products=self.request.user.cart.products, user=self.request.user
        )


class OrderDetailsViews(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderSellerViews(generics.ListAPIView):
    permission_classes = [IsSellerAndOwnerOrAdmin]


class OrderSellerDetailsViews(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSellerAndOwnerOrAdmin]
