from django.shortcuts import render

def cart(request):
    '''
    Render the cart page
    '''
    return render(request, 'cart/cart.html')

