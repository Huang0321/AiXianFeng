from rest_framework import filters
import django_filters

from AXF.models import User


class UserFilters(filters.FilterSet):

    class Meta:
        model = User
        fields = []
