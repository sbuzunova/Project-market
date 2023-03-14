from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
class Product(models.Model):
    name = models.CharField(max_length=255)
    discription = models.TextField(max_length=1000)
    price = models.IntegerField()
    image = models.ImageField()
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    size = models.CharField(max_length=5, default='S')
    maker = models.CharField(max_length=255, default='Китай')
    material = models.CharField(max_length=255, default='Бавовна')