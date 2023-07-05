from django.db import models


class Cart(models.Model):
    products = models.ManyToManyField(
        "product.Product", related_name="carts", blank=True
    )
