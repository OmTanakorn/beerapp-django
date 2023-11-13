from django_filters import rest_framework as filters
from Listbeers.models import Breweries,Beer

class BreweriesFilter(filters.FilterSet):
  name_contains = filters.CharFilter(field_name='name', lookup_expr='icontains')


  class Meta:
    model = Breweries
    fields = ["id","state"]