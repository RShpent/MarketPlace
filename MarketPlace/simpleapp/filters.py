from django_filters import FilterSet, CharFilter
from .models import Product


class ProductFilter(FilterSet):

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': ['lt'],
            'category': ['exact'],
        }
