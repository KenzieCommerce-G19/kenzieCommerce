from rest_framework import generics
from address.models import Address
from address.serializers import AddresseSerializer


class AddressView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddresseSerializer

    def get_object(self):
        user = self.request.user
        address = Address.objects.get(user=user)
        return address
