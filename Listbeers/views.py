from rest_framework.views import APIView
from Listbeers.models import Breweries,Beer
from Listbeers.serializers import BreweriesSerializers,BeerSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets
# Create your views here.

# class BeerViewSet(viewsets.ReadOnlyModelViewSet):
#   """
#     This viewset automatically provides `list` and `retrieve` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class BrewerisList(APIView):

  def get(self, request, format=None):
    breweries = Breweries.objects.all()
    serializer = BreweriesSerializers(breweries, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = BreweriesSerializers(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class BeerList(APIView):

  def get(self, request, format=None):
    beers = Beer.objects.all()
    serializer= BeerSerializer(beers,many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None):
    serializer = BeerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    