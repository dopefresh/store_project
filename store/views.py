from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib import messages
from django.views import generic
from .models import Item, OrderItem, Order


class HomeView(generic.ListView):
    model = Item
    paginate_by = 30
    template_name = 'store/home.html'
    context_object_name = 'items'    


def checkout(request):
    return render(request, 'store/checkout.html') 


def products(request): 
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'store/products.html', context)


def cart(request):
    context = {
        'order_items': OrderItem.objects.all() 
    }
    return render(request, 'store/cart.html', context)


def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f"This item quantity was updated to {order_item.quantity}")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to the cart")
    else:
        order = Order.objects.create(user=request.user, ordered_date=timezone.now())
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect(reverse('store:cart'))
    

def remove_from_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_item = get_object_or_404(OrderItem, item__pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    ) 
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item.delete()
    else:
        messages.info(request, "This item isn't in your cart") 
    return redirect(reverse('store:cart')) 


def decrease_amount_of_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_item = get_object_or_404(OrderItem, item__pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0] 
        if order.items.filter(item__pk=item.pk).exists():
            if order_item.quantity <= 1:
                order_item.delete()
            else:
                order_item.quantity -= 1
                order_item.save()
        else:
            messages.info(request, "This item quantity is already zero")
    return redirect(reverse('store:cart'))


