from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    fullName = models.CharField(max_length=128,null=True)
    telephone = models.CharField(max_length=10,null=True)
    email = models.EmailField(max_length=50,null=True)
    birthday = models.DateField(null=True)
    address = models.CharField(max_length=128,null=True)
  
    def __str__(self):
        return self.username


