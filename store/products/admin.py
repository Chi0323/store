from django.contrib import admin
from products.models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display=('title','content','specifications','price','quantity')

admin.site.register(Products,ProductsAdmin)
