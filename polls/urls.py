from django.urls import path
from .views import *

app_name = 'polls'

urlpatterns=[
	path('dashboard/', pollView, name='pollview'),
	path('vote/<int:poll_id>/', pollVote, name='pollvote'),
	path('vote/<int:poll_id>/results/', pollResult, name='pollresult'),
]
