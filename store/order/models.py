from django.db import models

class Order (models.Model):
    payment = models.CharField(max_length=20,choices = (('信用卡一次付清','信用卡一次付清'),('ATM付款','ATM付款'),('退貨/退款','退貨/退款'),('LINE PAY','LINE PAY'),('貨到付款','貨到付款')),null=True)
    fullName = models.CharField(max_length=128,null=True)
    telephone = models.CharField(max_length=10,null=True)
    phone = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=128,null=True)
    pubDateTime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.fullName
    class Meta:
        ordering = ['pubDateTime']
