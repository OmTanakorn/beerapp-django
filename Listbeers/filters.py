from django_filters import rest_framework as filters
from Listbeers.models import Breweries,Beer,Store

class BreweriesFilter(filters.FilterSet):
  name_contains = filters.CharFilter(field_name='name', lookup_expr='icontains')

  class Meta:
    model = Breweries
    fields = ["id","name","city"]

class StoreFilter(filters.FilterSet):
  beer_id = filters.NumberFilter(field_name='beer__id', lookup_expr='exact')
  beer_style = filters.CharFilter(field_name='beer__style',lookup_expr="icontains")
  
  class Meta:
    model = Store
    fields = ["id","name"]
  
class BeerFilter(filters.FilterSet):
  
  class Meta:
    model = Beer
    fields = ["id"]
