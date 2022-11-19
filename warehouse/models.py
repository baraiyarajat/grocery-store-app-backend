from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    default_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name
