from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField('email address',blank=True, max_length=254)
    birthday = models.CharField('date',blank=True, max_length=10)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)