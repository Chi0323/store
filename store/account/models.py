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


ASKTYPE=(('訂單','訂單'),('出貨','出貨'),('退貨/退款','退貨/退款'),('取消訂單','取消訂單'),('其他','其他')),

class Ask(models.Model):
    asktype = models.CharField(max_length=20,choices = (('訂單','訂單'),('出貨','出貨'),('退貨/退款','退貨/退款'),('取消訂單','取消訂單'),('其他','其他')),null=True)
    asktittle = models.CharField(max_length=128,null=True)
    ordernumber = models.CharField(max_length=128,null=True)
    suggest = models.CharField(max_length=128,null=True)
    pubDateTime = models.DateTimeField(auto_now_add=True)
  
  
    def __str__(self):
        return self.asktittle
