from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=400, unique=True)
    slug = models.SlugField(max_length=400, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    benefits = models.CharField(max_length=2000, blank=True, null=True)
    how_to_use = models.CharField(max_length=2000, blank=True, null=True)
    disclaimer = models.CharField(max_length=2000, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(max_length=255, null=True, upload_to='photos/product_primary_image')

    def __str__(self):
        return self.name
