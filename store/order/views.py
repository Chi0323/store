from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from order.models import Order
from order.forms import OrderForm
from product.models import Product


def order(request):
    '''
    Render the order page
    '''
    orders = Order.objects.all()
    print(orders)
    context = {'orders':orders}
    return render(request, 'order/order.html',context)

def orderCreate(request, productId):
    '''
    orderCreate a new order
    '''
    product = get_object_or_404(Product, id=productId)
    template = 'order/orderCreate.html'
    if request.method == 'GET':
        return render(request, template, {'orderForm':OrderForm(), 'product':product})

    # POST
    orderForm = OrderForm(request.POST)
    if not orderForm.is_valid():
        return render(request, template, {'orderForm':orderForm})

    order = orderForm.save(commit=False)
    product = get_object_or_404(Product, id=productId)
    order.product = product
    order.save()
    messages.success(request, '訂單已完成')
    return redirect('order:order')

def orderSearch(request, orderId):
    '''
    Read an order
        1. Get the "order" instance using "orderId"; redirect to the 404 page if not found
        2. Render the orderRead template with the order instance and its
           associated comments
    '''
    order = get_object_or_404(Order, id=orderId)
    context = {'order': order}
    return render(request, 'order/orderSearch.html', context)


