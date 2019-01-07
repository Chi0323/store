from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from product.models import Product
from product.forms import ProductForm


def product(request):
    '''
    Render the product page
    '''
    products = Product.objects.all()
    print(products)
    context = {'products': products}    
    
    return render(request,'product/product.html', context)

def productCreate(request):
    '''
    Create a new product instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the product page
    '''
    template = 'product/productCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'productForm':ProductForm()})
    
    # POST
    productForm = ProductForm(request.POST)
    if not productForm.is_valid():
        return render(request, template, {'productForm':productForm})

    productForm.save()
    messages.success(request, '商品已新增')
    return redirect('product:product')

def productRead(request, productId):
    '''
    Read an product
        1. Get the "product" instance using "productId"; redirect to the 404 page if not found
        2. Render the productRead template with the product instance and its
           associated comments
    '''
    product = get_object_or_404(Product, id=productId)
    context = {'product': product}
    return render(request, 'product/productRead.html', context)

def productUpdate(request, productId):
    '''
    Update the product instance:
        1. Get the product to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    product = get_object_or_404(Product, id=productId)
    template = 'product/productCreateUpdate.html'
    if request.method == 'GET':
        productForm = ProductForm(instance=product)
        return render(request, template, {'productForm':productForm})

    # POST
    productForm = ProductForm(request.POST, instance=product)
    if not productForm.is_valid():
        return render(request, template, {'productForm':productForm})

    productForm.save()
    messages.success(request, '產品已修改') 
    return redirect('product:productRead', productId=productId)

def productDelete(request, productId):
    '''
    Delete the product instance:
        1. Render the product page if the method is GET
        2. Get the product to delete; redirect to 404 if not found
    '''
    if request.method == 'GET':
        return product(request)

    # POST
    product = get_object_or_404(Product, id=productId)
    product.delete()
    messages.success(request, '文章已刪除')  
    return redirect('product:product')
