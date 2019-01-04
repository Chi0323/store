from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    specifications = models.CharField(max_length=128)
    price = models.IntegerField()
    quantity = models.IntegerField()                    
    
    def __str__(self):
        return self.title