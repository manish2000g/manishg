from django.shortcuts import render
from accounts.auth import admin_only
from livestocks.models import *
from django.contrib.auth.models import User

@admin_only
def dashboard(request):
    category = Category.objects.all()
    category_count = category.count()
    livestock = Livestock.objects.all()
    livestock_count = livestock.count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    context = {
        'category': category_count,
        'livestock': livestock_count,
        'user': user_count,
        'admin': admin_count
    }
    return render(request, 'admins/dashboard.html', context)
