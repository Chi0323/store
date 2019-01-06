from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.products, name='products'),
    path('productsCreate/', views.productsCreate, name='productsCreate'),
    path('productsRead/<int:productId>/', views.productsRead, name='productsRead'),
    path('productsUpdate/<int:productId>/', views.productsUpdate, name='productsUpdate'),
    path('productsDelete/<int:productId>/', views.productsDelete, name='productsDelete'),
]
