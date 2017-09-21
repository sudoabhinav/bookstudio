from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField


@python_2_unicode_compatible
class User(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    landmark = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=5, null=True, blank=True)
    gender = models.CharField(max_length=8, null=True, blank=True, choices=GENDER_CHOICES)
    country = CountryField(blank_label='(select country)', null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
