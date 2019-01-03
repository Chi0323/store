from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=20, null=False)
    content = models.TextField()
    specifications = models.CharField(max_length=20) 
    price = models.IntegerField(default=0, null=False)  
    quantity = models.IntegerField(default=0, null=False)
     

    def __str__(self):
        return self.title

    


    
    
    
