from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_superUser = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    address = models.OneToOneField(
        "address.address", on_delete=models.CASCADE, null=True
    )
    cart = models.OneToOneField("cart.cart", on_delete=models.CASCADE, null=True)
