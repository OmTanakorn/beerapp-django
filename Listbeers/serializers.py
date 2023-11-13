from rest_framework import serializers
from Listbeers.models import Breweries,Beer

class BreweriesSerializers(serializers.ModelSerializer):

  class Meta:
    model = Breweries
    fields = ['id','name','city']

  # def to_representation(self, instance):
  #   return super().to_representation(instance)
    
  # def to_internal_value(self, data):
  #   return super().to_internal_value(data)
  
  # def validate(self, attrs):
  #   return super().validate(attrs)

class BeerSerializer(serializers.ModelSerializer):
  brewery = serializers.SerializerMethodField(method_name='brewery_detail')
  brewery_name = serializers.CharField(source='brewery.name')

  def brewery_detail(self, instance):
    return instance.brewery.get_city_state()

  # def to_representation(self,instance ):
  #   print(instance.brewery)
  #   data = super().to_representation(instance)
  #   # brewery = representation.pop("brewery")
  #   data.update({'brewery':instance.brewery.get_city_state()})

  #   return data

# Use it for Input data #
  # def to_internal_value(self, data):
  #   if not data.get("abv",None):
  #     data["abv"] = 0.5
  #   if data.get("brewery")==0:
  #     data["brewery"] = 1
  #   if not data.get("style",None):
  #     data["style"]="IPA"
  #   return super().to_internal_value(data)
  
  class Meta:
    model = Beer
    fields = ['id','abv','name','style','brewery','ounces', 'brewery_name']