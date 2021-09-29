import django_filters
from .models import *
from django_filters import CharFilter

#
# class LivestockFilter(django_filters.FilterSet):
#     livestock_name_contains = django_filters.CharFilter(field_name='livestock_name', lookup_expr='icontains')
#
#     class Meta:
#         model = Livestock
#         fields = 'livestock_name'
