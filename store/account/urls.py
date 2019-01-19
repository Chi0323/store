from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.account, name='account'),
    path('askCreate/',views.askCreate,name='askCreate'),
    path('ask/',views.ask,name='ask'),
]
