from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from user.models import User
from product.models import Product
from product.serializers import ProductSerializer
from user.permissions import IsOwnerOrAdmin, IsSellerAndOwnerOrAdmin


# Create your views here.
class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]

    def perform_create(self, serializer: ProductSerializer) -> Product:
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        serializer.save(user=user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # sem a parte de verificar se é ou nao um vedendor
    # permission_classes = [IsAuthenticatedOrReadOnly, IsSellerAndOwnerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
