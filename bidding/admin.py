from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Category)
admin.site.register(Commodity)
admin.site.register(SeedType)
admin.site.register(Supplyside)
admin.site.register(Demandside)
admin.site.register(BidMatch)