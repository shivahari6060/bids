from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def pollView(request):
	polls = Poll.objects.all().order_by('-pub_date')[:5]
	context={
		'polls':polls,
	}
	return render(request, 'polls/polls_list.html', context)

def pollVote(request, poll_id):
	obj = get_object_or_404(Poll, pk=poll_id)
	choices= obj.choice_set.all()
	context={
		'poll':obj,
		'choices':choices,
	}
	return render(request, 'polls/polls_vote.html', context)

def pollResult(request, poll_id):
	obj = get_object_or_404(Poll, pk=poll_id)
	results= obj.get_result_dict
	votes= obj.vote_set.count()
	context={
		'poll':obj,
		'results': results,
		'votes':votes
	}
	return render(request, 'polls/polls_result.html', context)