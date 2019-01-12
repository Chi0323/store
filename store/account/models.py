from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.EmailField(max_length=50, unique=True)
    fullName = models.CharField(max_length=128,null=True)
    telephone = models.CharField(max_length=10,null=True)
    birthday = models.DateField(null=True)
    address = models.CharField(max_length=128,null=True)
    
    ASKTYPE=((1,'訂單'),(2,'出貨'),(3,'退貨/退款'),(4,'取消訂單'),(5,'其他'))
    asktype=models.CharField(max_length=1,choices=ASKTYPE,null=True)
    asktittle = models.CharField(max_length=128,null=True)
    ordernumber=models.CharField(max_length=128,null=True)
    suggest=models.CharField(max_length=128,null=True)
    def __str__(self):
        return self.fullName + ' (' + self.username + ')'


