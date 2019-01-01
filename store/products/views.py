from django.shortcuts import render

def products(request):
    '''
    Render the products page
    '''
    return render(request, 'products/products.html')

