from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
class Bucket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    status = models.IntegerField()
    full_name = models.CharField(max_length=255, blank=True, null=True)
    post_number = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)