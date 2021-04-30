from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    create_date = models.DateTimeField(auto_now_add=True)
