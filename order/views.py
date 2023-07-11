from rest_framework import generics
from rest_framework.views import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from order.models import Order
from user.models import User
from cart.models import Cart
from order.serializer import OrderSerializer
from user.permissions import (
    IsSellerAndOwnerOrAdmin,
    IsOwnerOrAdmin,
    IsSellerOrAdmin,
    IsProductSellerOrAdmin,
)
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from product.serializers import ProductSerializer

"""
loop for no products
    sellers = []
    sellers.append(products.user)
    converter sellers em set para tirar os duplicados
    converte novamente para array
    percorrer o sellers e para cada seller
    percorrer todos os produtos e filtrar pelo valor do seller e fazer o append
    transformar os arrays em somente um array


"""


class OrderViews(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data["user_id"])
        cart = Cart.objects.get(user=user)
        seller = User.objects.get(id=3)
        products = cart.products.all()
        print("texxxxtooooooo", products)
        # check quantity
        for product in products:
            if product.quantity == 0:
                raise isNotAvaliableError("product it's not avaliable")
        # new quantity
        for product in products:
            product.quantity = product.quantity - 1
            product.save()
            seller = []
            for product in products:
                seller.append(product.user)

            no_duplicate_seller = set(seller)
            seller_list = list(no_duplicate_seller)
            all_orders = []
            for seller in seller_list:
                order_seller_list = []
                for product in products:
                    seller_product = products.filter(product.user == seller)
                    order_seller_list.append(seller_product)
                all_orders.append(order_seller_list)

            for order in all_orders:
                order = serializer.save(
                    user=self.request.user,
                    seller=seller,
                )
                order.products.set(products)

        # serializer.save(products=cart.products, user=self.request.user)


class OrderDetailsViews(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderSellerViews(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsSellerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return Order.objects.get(seller=self.request.user)


class OrderSellerDetailsViews(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsProductSellerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if "status" in request.data:
            new_status = request.data["status"]
            send_mail(
                subject="Atualização no status do pedido",
                message=f"O status do seu pedido foi atualizado para: {new_status}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[instance.user.email],
                fail_silently=False,
            )

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
