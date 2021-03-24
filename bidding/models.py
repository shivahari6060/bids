from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class District(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Municipality(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

#the category and commodity of the supply and demand.
class Category(models.Model):
    name= models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Commodity(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    name= models.CharField(max_length=250)

    def __str__(self):
        return self.name
#the type of the propagation methods
class SeedType(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete= models.CASCADE)
    name= models.CharField(max_length=150)

    def __str__(self):
        return self.name

#the supply model and the demand model for the bidding.
class Supplyside(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    commodity = models.ForeignKey(Commodity, on_delete=models.SET_NULL, null=True)
    seed_type= models.ForeignKey(SeedType, on_delete=models.SET_NULL, null=True)
    quantity= models.IntegerField(default=0)
    price = models.FloatField()
    supply_create= models.DateTimeField(auto_now_add=True)
    supply_edit= models.DateTimeField(auto_now=True)
    supply_date = models.DateTimeField()
    zip_code= models.CharField(max_length=25, help_text="Enter google postal code")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    municipality= models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True)
    city= models.CharField(max_length=250)
    active= models.BooleanField(default=False)
    slug= models.CharField(max_length=250, default='maize')

    def __str__(self):
        return self.slug


class Demandside(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    commodity = models.ForeignKey(Commodity, on_delete=models.SET_NULL, null=True)
    seed_type= models.ForeignKey(SeedType, on_delete=models.SET_NULL, null=True)
    quantity= models.IntegerField(default=0)
    price = models.FloatField()
    supply_create= models.DateTimeField(auto_now_add=True)
    supply_edit= models.DateTimeField(auto_now=True)
    supply_date = models.DateTimeField()
    zip_code= models.CharField(max_length=25, help_text="Enter google postal code")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    municipality= models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True)
    city= models.CharField(max_length=250)
    active= models.BooleanField(default=False)
    slug= models.CharField(max_length=250, default='maize')

    def __str__(self):
        return self.slug

class BidMatch(models.Model):
    supply_id = models.IntegerField()
    demand_id = models.IntegerField()
    txn_code= models.CharField(max_length=100)
    category= models.CharField(max_length=100, null=True)
    commodity= models.CharField(max_length=100, null=True)
    seed_type= models.CharField(max_length=100, null=True)
    quantity= models.IntegerField(default=0)
    price= models.FloatField( default=0)
    created= models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.txn_code

    @property
    def get_total(self):
        return self.quantity * self.price
    


