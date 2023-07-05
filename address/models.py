from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100, blank=True)
    number = models.IntegerField(null=True, blank=True)
    district = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
