from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework import generics


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer: UserSerializer) -> User:
        user = serializer.save()

        address_data = self.request.data.get("address")
        if address_data:
            address_data["user"] = user
        else:
            address_data = {
                "user": user,
            }

        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()

        cart_data = {
            "user": user,
        }
        cart_serializer = CartSerializer(data=cart_data)
        cart_serializer.is_valid(raise_exception=True)
        cart_serializer.save()

        return user


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer
