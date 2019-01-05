from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Products
from products.forms import ProductsForm


def products(request):
    '''
    Render the products page
    '''
    products = Products.objects.all()
    print(products)

    context = {'products': products,}    
    
    return render(request,'products/products.html', context)

def productsCreate(request):
    '''
    Create a new products instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the products page
    '''
    template = 'products/productsCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'productsForm':ProductsForm()})
    
    # POST
    productsForm = ProductsForm(request.POST)
    if not productsForm.is_valid():
        return render(request, template, {'productsForm':productsForm})

    productsForm.save()
    messages.success(request, '商品已新增')
    return redirect('products:products')

def productsRead(request, productsId):
    '''
    Read an products
        1. Get the "products" instance using "productsId"; redirect to the 404 page if not found
        2. Render the productsRead template with the products instance and its
           associated comments
    '''
    products = get_object_or_404(Products, id=productsId)
    context = {'products': products,}
    return render(request, 'products/productsRead.html', context)

def productsUpdate(request, productsId):
    '''
    Update the products instance:
        1. Get the products to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    products = get_object_or_404(Products, id=productsId)
    template = 'products/productsCreateUpdate.html'
    if request.method == 'GET':
        productsForm = ProductsForm(instance=products)
        return render(request, template, {'productsForm':productsForm})

    # POST
    productsForm = ProductsForm(request.POST, instance=products)
    if not productsForm.is_valid():
        return render(request, template, {'productsForm':productsForm})

    productsForm.save()
    messages.success(request, '產品已修改') 
    return redirect('products:productsRead', productsId=productsId)

def productsDelete(request, productstId):
    '''
    Delete the product instance:
        1. Render the products page if the method is GET
        2. Get the products to delete; redirect to 404 if not found
    '''
    if request.method == 'GET':
        return products(request)

    # POST
    products = get_object_or_404(Products, id=productstId)
    products.delete()
    messages.success(request, '文章已刪除')  
    return redirect('products:products')
