from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=127)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    isAvailable = models.BooleanField(default=True)
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="products"
    )