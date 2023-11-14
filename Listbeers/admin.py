from django.contrib import admin
from .models import Store, Beer

@admin.register(Beer)
class Beer(admin.ModelAdmin):
    list_display = ['name', 'abv', 'style']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'local', 'display_beers']

    def display_beers(self, obj):
        return ", ".join([beer.name for beer in obj.beer.all()])
    
    display_beers.short_description = "Beers"


