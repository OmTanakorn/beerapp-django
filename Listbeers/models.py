from django.db import models


class Breweries(models.Model):
    name = models.TextField()
    city = models.TextField()    

    # def get_city_state(self):
    #     return self.city + " " + self.state

class Beer(models.Model):
    abv = models.FloatField(default=0.5)
    name = models.TextField()
    style = models.TextField()
    brewery = models.ForeignKey(Breweries, related_name='brewery_beers', on_delete=models.CASCADE)
    ounces = models.FloatField()

class Store(models.Model):
    name = models.TextField()
    local = models.TextField()
    beer = models.ManyToManyField(Beer)

#     @property
#     def show_name(self):
#         return self.name + " " + self.style
    
#     @staticmethod
#     def x():
#         return 10
    

#  beers = Beer.objects.all()
# for no, beer in enumerate(beers):
#     data = beer.__dict__
#     data.update({"no": no})
#     print(data)


