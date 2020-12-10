import django_filters
from .models import *


class LibAdminFilter(django_filters.FilterSet):
    class Meta:
        model = LibAdmin
        fields = ['book', 'customer']
