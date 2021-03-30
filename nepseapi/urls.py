from django.urls import path
from .views import *

app_name="nepseapi"

urlpatterns=[
	path('api/nepse/data/', NepseApi.as_view(), name='nepseapi')

]