from rest_framework import generics
from address.models import Address
from address.serializers import AddresseSerializer

from user.permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated


class AddressView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Address.objects.all()
    serializer_class = AddresseSerializer
