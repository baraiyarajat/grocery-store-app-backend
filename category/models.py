from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='photos/categories', max_length=255, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
