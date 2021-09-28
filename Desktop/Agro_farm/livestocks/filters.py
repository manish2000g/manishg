import django_filters
from .models import *


class LivestockFilter(django_filters.FilterSet):
    class Meta:
        model = Livestock
        fields = '__all__'
        exclude =