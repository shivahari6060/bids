from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, JsonResponse

# Create your views here.

def pollView(request):
	polls = Poll.objects.all().order_by('-pub_date')[:5]
	context={
		'polls':polls,
	}
	return render(request, 'polls/polls_list.html', context)


#voting page 
# @login_required(login_url='/login/')
@login_required()
def pollVote(request, poll_id):
	obj = get_object_or_404(Poll, pk=poll_id)
	choices= obj.choice_set.all()
	if request.method=='POST':
		try:
			#select choice from request POST 
			selected_choice=obj.choice_set.get(pk=request.POST['choice'])
		except (KeyError, Choice.DoesNotExist):
			return render(request, 'polls/polls_vote.html', context={'poll':obj, 'message':"You didn't select any option ! Please Select.", 'choices':choices})
		user= request.user
		vote= Vote.objects.create(user=user, poll=obj, choice=selected_choice )
		return HttpResponseRedirect(reverse('polls:pollresult', args=[str(obj.id)]))
	context={
		'poll':obj,
		'choices':choices,
	}
	return render(request, 'polls/polls_vote.html', context)
#result jsonResponse
def ResultJson(request, poll_id):
	labels=[]
	votes=[]
	percentage=[]
	obj = get_object_or_404(Poll, pk=poll_id)
	for result in obj.choice_set.all():
		labels.append(result.choice_text)
		votes.append(result.get_vote_count)
		pct=(result.get_vote_count/obj.get_vote_count)*100
		perct=round(pct, 2)
		percentage.append(perct)
	data={
		'labels':labels,
		'votes':votes,
		'percentage':percentage,
		'label':obj.text
	}
	return JsonResponse(data, safe=False)


#result page
def pollResult(request, poll_id):
	obj = get_object_or_404(Poll, pk=poll_id)
	results= obj.get_result_dict
	total_votes= obj.vote_set.count()
	context={
		'poll':obj,
		'results': results,
		'total_votes':total_votes
	}
	return render(request, 'polls/polls_result.html', context)


class PollResult(APIView):
 
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk=None, format=None):
    	labels=[]
    	votes=[]
    	obj= get_object_or_404(Poll, pk=pk)
    	for result in obj.choice_set.all():
    		labels.append(result.choice_text)
    		votes.append(result.get_vote_count)
    	print(labels)
    	data={
    		'labels':labels,
    		'votes':votes
    	}
    	return Response(data)