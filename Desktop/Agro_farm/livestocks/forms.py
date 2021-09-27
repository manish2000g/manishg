from django import forms
from django.forms import ModelForm

from .models import Category, Livestock, Order

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class LivestockForm(ModelForm):
    class Meta:
        model = Livestock
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'contact_no', 'contact_address', 'payment_method']