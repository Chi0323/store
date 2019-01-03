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
    template = 'products/articleCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'productsForm':ProductsForm()})
    
    # POST
    productsForm = ProductsForm(request.POST)
    if not productsForm.is_valid():
        return render(request, template, {'productsForm':productsForm})

    productsForm.save()
    messages.success(request, '商品已新增')
    return redirect('products:products')

def productsUpdate(request, productsId):
    '''
    Update the article instance:
        1. Get the article to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    #products = get_object_or_404(Products, id=productsId)
    template = 'products/productsCreateUpdate.html'
    if request.method == 'GET':
        productsForm = ProductsForm(instance=products)
        return render(request, template, {'productsForm':productsForm})

    # POST
    productsForm = ProductsForm(request.POST, instance=products)
    if not productsForm.is_valid():
        return render(request, template, {'productsForm':productsForm})

    productsForm.save()
    messages.success(request, '文章已修改') 
    return redirect('products:products', productsId=productsId)

