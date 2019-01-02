from django.contrib import admin
from products.models import Products,two


class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['title','content','price' ]
    fields = ('title','content','price' )
    
class twoModelAdmin(admin.ModelAdmin):
    list_display = ['specifications','quantity']
    fields = ('specifications','quantity')    

 

admin.site.register(Products,ProductsModelAdmin)
admin.site.register(two,twoModelAdmin)