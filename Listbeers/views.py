from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from Listbeers.models import Breweries,Beer
from Listbeers.serializers import BreweriesSerializers,BeerSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import generics
from .filters import BreweriesFilter

# Create your views here.
 
class BreweriesList(generics.ListAPIView):
    queryset = Breweries.objects.all()
    serializer_class = BreweriesSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = BreweriesFilter
    
class BeerList(generics.ListAPIView):
    serializer_class = BeerSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id')
        if id is None:
            queryget = Beer.objects.all()
            return queryget
        queryget = Beer.objects.filter(id__gte=id)
        print(queryget)
        return queryget

# class BeerState(generics.ListAPIView):
#     serializer_class = BeerSerializer
    
#     def get_queryset(self):
#         queryset = Beer.objects.all()
#         stateset = Breweries.objects.all()
#         state = self.request.query_params.get('state')

#         if stateset is not None:
#             stateset = stateset.filter(state=state)
#             for brewery in stateset:
#                 print(brewery.id) 
#             queryset = queryset.filter(brewery__in=stateset)

#         return queryset


# class BrewerisList(APIView):

#   def get(self, request, format=None):
#     breweries = Breweries.objects.all()
#     serializer = BreweriesSerializers(breweries, many=True)
#     return Response(serializer.data)

#   def post(self, request, format=None):
#     serializer = BreweriesSerializers(data=request.data)

#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
# class BeerList(APIView):

#   def get(self, request, format=None):
#     beers = Beer.objects.all()
#     serializer= BeerSerializer(beers,many=True)
#     return Response(serializer.data)
  
#   def post(self, request, format=None):
#     serializer = BeerSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)