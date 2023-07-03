from django.db import models
from django.contrib.auth.models import AbstractUser

from product.models import Product
from user.models import User


class Cart(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product, through="CartItem", related_name="cart_item"
    )
