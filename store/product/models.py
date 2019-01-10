from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    brand = models.CharField(max_length=128)
    specifications = models.CharField(max_length=128)    
    price = models.IntegerField()
    quantity = models.IntegerField()                   
    
    def __str__(self):
        return self.title
    

