from django.shortcuts import render, redirect
from django.contrib import messages
from order.models import Order
from order.forms import OrderForm

def order(request):
    '''
    Render the order page
    '''
    orders = Order.objects.all()
    print(orders)
    context = {'orders':orders}
    return render(request, 'order/order.html',context)

def orderCreate(request):
    '''
    orderCreate a new order
    '''
    template = 'order/orderCreate.html'
    if request.method == 'GET':
        return render(request, template, {'orderForm':OrderForm()})

    # POST
    orderForm = OrderForm(request.POST)
    if not orderForm.is_valid():
        return render(request, template, {'orderForm':orderForm})

    orderForm.save()
    messages.success(request, '訂單已完成')
    return redirect('order:order')