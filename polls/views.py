from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required

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

#result page
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