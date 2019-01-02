from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() 
    price = models.IntegerField(default=0)   

    def __str__(self):
        return self.title
    
class two(models.Model):
    specifications = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)


    
    
    
