from django.shortcuts import render, redirect

from products.models import Products
from products.forms import ProductsForm
from django.contrib import messages

def products(request):
    '''
    Render the products page
    '''
    products = Products.objects.all()
    context = {'products':products}
    
    return render(request, 'products/products.html', context)

def productsCreate(request):
    '''
    Create a new products instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the products page
    '''
    template = 'products/productsCreate.html'
    if request.method == 'GET':
        return render(request, template, {'productsForm':ProductsForm()})
    
    # POST
    productsForm = ProductsForm(request.POST)
    if not productsForm.is_valid():
        return render(request, template, {'productsForm':productsForm})

    productsForm.save()
    messages.success(request, '商品已新增')
    return redirect('products:products')

