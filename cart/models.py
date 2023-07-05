from django.db import models
from django.contrib.auth.models import AbstractUser

from product.models import Product
from user.models import User


class Cart(models.Model):
    products = models.ManyToManyField(Product, related_name="carts", blank=True)
