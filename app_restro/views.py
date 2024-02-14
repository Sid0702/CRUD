# app_restro/views.py

from django.shortcuts import get_object_or_404, render, redirect
from .models import Order

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        new_order = Order.objects.create(name=name, item=item, quantity=quantity, price=price)
        new_order.save()
        return redirect('order_display')
    return render(request, 'html_pages/index.html')

def order_display(request):
    orders = Order.objects.all()
    return render(request, 'html_pages/order_display.html', {'orders': orders})

def edit_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)

    if request.method == 'POST':
        order.name = request.POST.get('name')
        order.item = request.POST.get('item')
        order.quantity = request.POST.get('quantity')
        order.price = request.POST.get('price')
        order.save()
        return redirect('order_display')

    return render(request, 'html_pages/edit_order.html', {'order': order})

def delete_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('order_display')

    return render(request, 'html_pages/delete_order.html', {'order': order})
