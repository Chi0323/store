from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.EmailField(max_length=50, unique=True)
    fullName = models.CharField(max_length=128)
    telephone = models.CharField(max_length=10, blank=False)
    birthday = models.DateField(blank=False)
    address = models.CharField(max_length=128, blank=False)



    def __str__(self):
        return self.fullName + ' (' + self.username + ')'


