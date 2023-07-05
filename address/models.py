from django.db import models
from django.contrib.auth.models import AbstractUser

from user.models import User


class Address(models.Model):
    street = models.CharField(max_length=100, blank=False)
    number = models.IntegerField(blank=False)
    districk = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)
    zip_code = models.CharField(blank=False)
