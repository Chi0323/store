from django.contrib import admin
from order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['payment', 'fullName', 'telephone','phone', 'address']
    search_fields = ['payment']
admin.site.register(Order,OrderAdmin)
