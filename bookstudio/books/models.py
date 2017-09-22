from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    pages = models.CharField(max_length=5)
    price = models.CharField(max_length=6)
    description = models.TextField(null=True, blank=True)
