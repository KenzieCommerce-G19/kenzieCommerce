from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from user.models import User
from product.models import Product
from product.serializers import ProductSerializer
from user.permissions import IsSellerAndOwnerOrAdminOrReadOnly, IsSellerOrAdmin


# Create your views here.
class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer: ProductSerializer) -> Product:
        serializer.save(user=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerAndOwnerOrAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
