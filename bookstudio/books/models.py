from django.db import models
from bookstudio.users.models import User


class Book(models.Model):
    name = models.CharField(max_length=40)
    user_name = models.ForeignKey(User, null=True, blank=True)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    pages = models.CharField(max_length=5)
    price = models.CharField(max_length=6)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user_name.username
