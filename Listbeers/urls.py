from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from Listbeers import views

urlpatterns = [
  path('breweries/',views.BreweriesList.as_view(),name="breweries-list"),
  path('beer/',views.BeerList.as_view()),
  # path('beerstate/',views.BeerState.as_view()),
  re_path('^breweries/(?P<id>.+)/$',views.BreweriesList.as_view()),
  re_path('^beer/(?P<id>.+)/$',views.BeerList.as_view()),
  # re_path('^beerstate/(?P<state>.+)/$',views.BeerState.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)