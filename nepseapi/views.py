from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import requests
from bs4 import BeautifulSoup
import pandas as pd 
import json

def GoogleDrive(request):
	context={}
	return render(request, 'nepseapi/googledrive.html', context)

# Create your views here.

def get_range(request, maxm):
	rng=[]
	for i in range(1, maxm):
		rng.append(i)
	return rng

		
def get_url(request):
	rng= get_range(request, 12)
	table_Datas=[]
	for i in rng:
		_id = i
		url = "http://www.nepalstock.com/main/todays_price/index/%s" % _id
		headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
		gethtml = requests.get(url, headers)
		html = gethtml.text
		bs = BeautifulSoup(html, 'html.parser')
		table = bs.find('table',{'class':'table'})
		rows = table.findAll('tr')
		for td in rows:
			t_d = td.findAll('td')
			for tD in t_d:
				table_Datas.append(td.text.strip())
	return table_Datas


class NepseApi(APIView):
	authentication_classes = []
	permission_classes = []
	def get(self, request, format=None):
		level2=[]
		rng=get_range(request, 8)
		table_Datas=get_url(request)
		level1= pd.Series(table_Datas).drop_duplicates().tolist()

		for k in level1:
			if len(k)> 35:
				level2.append(k)
			else:
				pass
		d=[]
		for l in range(1, len(level2)):
			c= level2[l].split('\n')
			d.append(c)
		df= pd.DataFrame(d[1:], columns=d[0])
		date= pd.Timestamp.today().strftime('%Y-%m-%d')
		df['date']= date
		df_csv = df.to_csv(date +'.csv', index=False)
		df.rename(columns={'Traded Companies': 'company_name','No. Of Transaction': 'no_of_transaction', 'Max Price':'max_price','Min Price':'min_price','Closing Price':'closing_price','Traded Shares':'traded_shares','Previous Closing':'previous_closing','Difference Rs.':'difference_rs'}, inplace=True)
		jsn = json.loads(df.to_json(orient='records'))

		return Response(jsn)
		


    # def get(self, request, format=None):
    # 	cat=[]
    # 	val=[]
    # 	for category in Category.objects.all().distinct():
    # 		cat.append(category.name)
    # 		commodity_count= category.commodity_set.count()
    # 		val.append(commodity_count)
    # 	data={
    # 		'labels': cat,
    # 		'values': val,
    # 		}
    # 	return Response(data)