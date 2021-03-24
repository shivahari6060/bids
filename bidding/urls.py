from django.urls import path
from .views import *

app_name = 'bidding'

urlpatterns = [
    path('', index, name='bidding'),
    path('matchdemand', MatchDemand, name='matchdemand'),
    path('supplier_add', Supplier_add, name='supplier_add'),
    path('demand_add', Demand_add, name='demand_add'),

    path('ajax/load-provinces/', load_provinces, name='ajax_load_provinces'),
    path('ajax/load-districts/', load_districts, name='ajax_load_districts'),
    path('ajax/load-municipalities/', load_municipalities, name='ajax_load_municipalities'),
    path('ajax/load-commodity/', load_commodity, name='ajax_load_commodity'),
    path('ajax/load-seedtype/', load_seedtype, name='ajax_load_seedtype'),
    
]