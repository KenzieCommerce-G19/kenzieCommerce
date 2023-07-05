from django.db import models
from user.models import User
from product.models import Product


class Status(models.TextChoices):
    REQUEST_MAID = "Request_maid"
    IN_PROGRESS = "In_Progress"
    DELIVERED = "Delivered"
    DEFAULT = "Not informed"


class Order(models.Model):
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.DEFAULT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="orders"
    )
    product = models.ManyToManyField(
        "product.Product", related_name="order", blank=True
    )
