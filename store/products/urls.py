from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.products, name='products'),
    path('productsCreate/', views.productsCreate, name='productsCreate'),
]
