from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from product.models import Product
from product.serializers import ProductSerializer
from user.permissions import IsSellerAndOwnerOrAdminOrReadOnly, IsSellerOrAdminOrReadOnly


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer: ProductSerializer) -> Product:
        serializer.save(user=self.request.user)
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        category = self.request.query_params.get("category")

        queryset = queryset.filter(name__icontains=name) if name else queryset
        queryset = queryset.filter(category=category) if category else queryset

        return queryset

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerAndOwnerOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
