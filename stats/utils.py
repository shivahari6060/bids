# import matplotlib.pyplot as plt 
# import base64
# from io import BytesIO

# def get_graph():
# 	buffer = BytesIO()
# 	plt.savefig(buffer, format='png')
# 	buffer.seek(0)
# 	image_png = buffer.getvalue()
# 	grph = base64.base64encode(image_png)
# 	graph = graph.decode('utf-8')
# 	buffer.close()
# 	return graph

# def get_plot(x, y):
# 	plt.switch_backend('AGG')
# 	plt.figure(figsize=(10,5))
# 	plt.title('Sales of Item')
# 	plt.plot(x, y)
# 	plt.xticks(rotation=45)
# 	plt.xlabel('Item')
# 	plt.ylabel('Price')
# 	plt.tight_layout()
# 	graph = get_graph()
# 	return graph

# #views.py
# def main_view(request):
# 	qs = Sale.objects.all()
# 	x= [x.item for x in qs]
# 	y= [y.price for y in qs]
# 	chart= get_plot(x, y)

# #html page
# if chart
# img src="data:image/png;base64, {{chart|safe}}"