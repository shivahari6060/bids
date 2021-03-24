from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bidding.models import *

# Create your views here.
def statView(request):
	context={}
	return render(request, 'stats/stat_view.html', context)


class ChartData(APIView):
 
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
    	cat=[]
    	val=[]
    	for category in Category.objects.all().distinct():
    		cat.append(category.name)
    		commodity_count= category.commodity_set.count()
    		val.append(commodity_count)
    	data={
    		'labels': cat,
    		'values': val,
    		}
    	return Response(data)