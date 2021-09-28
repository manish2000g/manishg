from django.shortcuts import render, redirect
from .forms import CategoryForm, LivestockForm, OrderForm
from django.contrib import messages
from .models import Category, Livestock, Cart, Order
from accounts.auth import admin_only, user_only
from django.contrib.auth.decorators import login_required
import os



def homepage(request):
    return render(request, 'livestocks/homepage.html')

@login_required
@admin_only
def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect("/livestocks/get_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add category')
            return render(request, 'livestocks/category_form.html', {'form_category': form})
    context = {
        'form_category': CategoryForm,
        'activate_category': 'active'
    }
    return render(request, 'livestocks/category_form.html', context)


@login_required
@admin_only
def get_category(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'activate_category': 'active'
    }
    return render(request, 'livestocks/get_category.html', context)


@login_required
@admin_only
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category Deleted Successfully')
    return redirect('/livestocks/get_category')

@login_required
@admin_only
def category_update_form(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category updated successfully')
            return redirect("/livestocks/get_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update category')
            return render(request, 'livestocks/category_update_form.html', {'form_category':form})
    context ={
        'form_category': CategoryForm(instance=category),
        'activate_category': 'active'
    }
    return render(request, 'livestocks/category_update_form.html', context)




@login_required
@admin_only
def livestock_form(request):
    if request.method == "POST":
        form = LivestockForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Livestock added successfully')
            return redirect("/livestocks/get_livestock")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Livestock')
            return render(request, 'livestocks/livestock_form.html', {'livestock_food': form})
    context ={
        'form_livestock': LivestockForm,
        'activate_livestock': 'active'
    }
    return render(request, 'livestocks/livestock_form.html', context)


@login_required
@admin_only
def get_livestock(request):
    livestocks = Livestock.objects.all().order_by('-id')
    context = {
        'livestocks': livestocks,
        'activate_livestock': 'active'
    }
    return render(request, 'livestocks/get_livestock.html', context)


@login_required
@admin_only
def delete_livestock(request, livestock_id):
    livestock = Livestock.objects.get(id=livestock_id)
    os.remove(livestock.food_image.path)
    livestock.delete()
    messages.add_message(request, messages.SUCCESS, 'Livestock Deleted Successfully')
    return redirect('/livestocks/get_livestock')


@login_required
@admin_only
def livestock_update_form(request, livestock_id):
    livestock = Livestock.objects.get(id=livestock_id)
    if request.method == "POST":
        if request.FILES.get('livestock_image'):
            os.remove(livestock.livestock_image.path)
        form = LivestockForm(request.POST, request.FILES, instance=livestock)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Livestock updated successfully')
            return redirect("/livestocks/get_livestock")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update livestock')
            return render(request, 'livestocks/livestock_form.html', {'form_livestock':form})
    context ={
        'form_livestock': LivestockForm(instance=livestock),
        'activate_livestock': 'active'
    }
    return render(request, 'livestocks/livestock_update_form.html', context)


@login_required
@user_only
def show_categories(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_category_user': 'active'
    }
    return render(request, 'livestocks/show_categories.html', context)

@login_required
@user_only
def show_livestocks(request):
    livestocks = Livestock.objects.all().order_by('-id')
    context = {
        'livestocks': livestocks,
        'activate_livestock_user': 'active'
    }
    return render(request, 'livestocks/show_livestocks.html', context)

@login_required
@user_only
def checklist(request):
    categories  = Category.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_checklist':'active'
    }
    return render(request, 'livestocks/checklist.html', context)


@login_required
@user_only
def add_to_cart(request, livestock_id):
    user = request.user
    livestock = Livestock.objects.get(id=livestock_id)

    check_item_presence = Cart.objects.filter(user=user, livestock=livestock)
    if check_item_presence:
        messages.add_message(request, messages.ERROR, 'Item is already present in cart')
        return redirect('/livestocks/get_livestock_user')
    else:
        cart = Cart.objects.create(livestock=livestock, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Item added to cart')
            return redirect('/livestocks/mycart')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add item to cart')


@login_required
@user_only
def show_cart_items(request):
    user = request.user
    items = Cart.objects.filter(user= user)
    context = {
        'items': items,
        'activate_my_cart':'active'
    }
    return render(request, 'livestocks/mycart.html', context)


@login_required
@user_only
def remove_cart_item(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Cart item removed successfully')
    return redirect('/livestocks/mycart')


@login_required
@user_only
def order_form(request, livestock_id, cart_id):
    user = request.user
    livestock = Livestock.objects.get(id=livestock_id)
    cart_item = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = request.POST.get('quantity')
            price = livestock.livestock_price
            total_price = int(quantity) * int(price)
            contact_no = request.POST.get('contact_no')
            contact_address = request.POST.get('contact_address')
            payment_method = request.POST.get('payment_method')
            order = Order.objects.create(livestock=livestock,
                                         user=user,
                                         quantity=quantity,
                                         total_price=total_price,
                                         contact_no=contact_no,
                                         contact_address=contact_address,
                                         status="Pending",
                                         payment_method=payment_method,
                                         payment_status=False
                                         )
            if order:
                messages.add_message(request, messages.SUCCESS, 'Item Ordered. Continue Payment for Verification ')
                cart_item.delete()
                context = {
                    'order': order,
                    'cart': cart_item
                }
                return render(request, 'livestocks/esewa_payment.html', context)
        else:
                messages.add_message(request, messages.ERROR, 'Something went wrong')
                return render(request, 'livestocks/order_form.html', {'order_form': form})

    context = {
        'order_form': OrderForm
    }
    return render(request,'livestocks/order_form.html', context)


# import requests as req
def esewa_verify(request):
    import xml.etree.ElementTree as ET
    o_id = request.GET.get('oid')
    amount = request.GET.get('amt')
    refId = request.GET.get('refId')
    url = "https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amount,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid': o_id,
    }
    resp = request.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == 'Success':
        order_id = o_id.split("_")[0]
        order = Order.objects.get(id=order_id)
        order.payment_status = True
        order.save()
        cart_id = o_id.split("_")[1]
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        messages.add_message(request, messages.SUCCESS, 'Payment Successful')
        return redirect('/livestocks/mycart')
    else:
        messages.add_message(request, messages.ERROR, 'Unable to make payment')
        return redirect('/livestocks/mycart')


@login_required
@user_only
def my_order(request):
    user = request.user
    items = Order.objects.filter(user=user).order_by('-id')
    context = {
        'items':items,
        'activate_myorders':'active'
    }
    return render(request, 'livestocks/my_order.html', context)