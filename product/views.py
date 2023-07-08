from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from product.models import Product
from product.serializers import ProductSerializer
from user.permissions import (
    IsSellerAndOwnerOrAdminOrReadOnly,
    IsSellerOrAdminOrReadOnly,
)
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    pagination_class = CustomPagination
    ordering = "id"

    def perform_create(self, serializer: ProductSerializer) -> Product:
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        category = self.request.query_params.get("category")

        queryset = queryset.filter(name__icontains=name) if name else queryset
        queryset = (
            queryset.filter(category__icontains=category) if category else queryset
        )

        return queryset


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerAndOwnerOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
