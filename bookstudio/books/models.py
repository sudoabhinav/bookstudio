from django.db import models
from bookstudio.users.models import User
from storages.backends.s3boto import S3BotoStorage
import environ

env = environ.Env()



def books_directory_path(request, filename):
    return 'books/{0}/{1}'.format(request.user_name, filename)

class Book(models.Model):
    name = models.CharField(max_length=40)
    user_name = models.ForeignKey(User, null=True, blank=True)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    pages = models.CharField(max_length=5)
    price = models.CharField(max_length=6)
    description = models.TextField(null=True, blank=True)
    file_name = models.FileField(upload_to=books_directory_path, null=True, blank=True)

    def __str__(self):
        return self.user_name.username
