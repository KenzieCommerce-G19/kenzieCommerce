from django.db import models
from user.models import User
from product.models import Product


class Status(models.TextChoices):
    IN_PROGRESS = "In_Progress"
    DELIVERED = "Delivered"
    DEFAULT = "Request_maid"


class Order(models.Model):
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.DEFAULT
    )
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="orders"
    )
    seller = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="seller_orders"
    )
    products = models.ManyToManyField(
        "product.Product", related_name="order", blank=True
    )
