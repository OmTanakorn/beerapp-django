from rest_framework import serializers
from Listbeers.models import Breweries,Beer

class BreweriesSerializers(serializers.ModelSerializer):

  class Meta:
    model = Breweries
    fields = '__all__'

  # def to_representation(self, instance):
  #   return super().to_representation(instance)
    
  # def to_internal_value(self, data):
  #   return super().to_internal_value(data)
  
  # def validate(self, attrs):
  #   return super().validate(attrs)

class BeerSerializer(serializers.ModelSerializer):
  brewery_name=""
  
  
  def to_representation(self,instance ):
    print(instance.brewery)
    representation = super().to_representation(instance)
    # brewery = representation.pop("brewery")
    representation.update({'brewery':instance.brewery.name +","+instance.brewery.city})

    return representation

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
    fields = ['id','abv','name','style','brewery','ounces']