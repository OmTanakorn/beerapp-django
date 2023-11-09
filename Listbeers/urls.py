from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Listbeers import views

urlpatterns = [
  path('breweries/',views.BrewerisList.as_view()),
  path('beer/',views.BeerList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)