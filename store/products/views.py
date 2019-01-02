from django.shortcuts import render

from products.forms import productsForm

def products(request):
    '''
    Render the products page
    '''
    return render(request, 'products/products.html')

def productsCreate(request):
    '''
    Create a new products instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the products page
    '''
    template = 'products/productsCreate.html'
    if request.method == 'GET':
        return render(request, template, {'productsForm':productsForm()})

