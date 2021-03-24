from django.urls import path
from .views import *

app_name = 'stats'

urlpatterns=[
	path('stat_view/', statView, name='statview'),
	path('api/chart/data/', ChartData.as_view(), name='chartdata'),
]