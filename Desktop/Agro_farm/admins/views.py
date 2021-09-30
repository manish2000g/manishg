from django.shortcuts import render, redirect
from accounts.auth import admin_only
from livestocks.models import *
from livestocks.models import Order
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@admin_only
def dashboard(request):
    category = Category.objects.all()
    category_count = category.count()
    livestock = Livestock.objects.all()
    livestock_count = livestock.count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    order = Order.objects.all()
    order_count = order.count()
    context = {
        'category': category_count,
        'livestock': livestock_count,
        'user': user_count,
        'admin': admin_count,
        'order_count': order_count
    }
    return render(request, 'admins/dashboard.html', context)

@login_required
@admin_only
def all_orders(request):
    orders = Order.objects.all().order_by("-id")
    context = {
        'orders': orders,
        'activate_orders': 'active'
    }
    return render(request,'admins/orders.html',context)


@login_required
@admin_only
def delete_order(request, delete_id):
    order = Order.objects.get(id=delete_id)
    order.delete()
    messages.add_message(request, messages.SUCCESS, 'Order has been deleted successfully')
    return redirect('/admins/all_orders')

def delivered(request, id):
    mod = Order.objects.get(id=id)
    mod.status = "Delivered"
    mod.save()
    return redirect("/admins/all_orders")
def pending(request, id):
    mod = Order.objects.get(id=id)
    mod.status = "Pending"
    mod.save()
    return redirect("/admins/all_orders")
