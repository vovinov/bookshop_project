from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()


class Product(models.Model):
    pass
