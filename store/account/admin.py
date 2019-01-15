from django.contrib import admin
from account.models import User,Ask

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'fullName', 'telephone', 'telephone', 'birthday', 'address']
    search_fields = ['username']

class AskAdmin(admin.ModelAdmin):
    list_display = ['asktittle', 'asktype', 'ordernumber', 'suggest']
    search_fields = ['asktittle']
admin.site.register(User,UserAdmin)
admin.site.register(Ask,AskAdmin)