from django.urls import path
from order import views

app_name = 'order'
urlpatterns = [
    path('', views.order, name='order'),
    path('orderCreate/<int:productId>/', views.orderCreate, name='orderCreate'),
    path('orderSearch/<int:orderId>/', views.orderSearch, name='orderSearch'),
    
]
