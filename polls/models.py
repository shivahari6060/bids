from django.db import models

from django.conf import settings
# from django.contrib.auth.models import User
# settings.AUTH_USER_MODEL
# Create your models here.

class Poll(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text= models.CharField(max_length= 250)
	pub_date= models.DateTimeField(auto_now_add=True)
	active= models.BooleanField(default=False)

	def __str__(self):
		return self.text

	def user_can_vote(self, user):
		user_votes= user.vote_set.all()
		qs = user_votes.filter(poll=self)
		if qs.exists():
			return False
		return True

#this property counts the total votes that had been voted in selected question 
	@property
	def get_vote_count(self):
		return self.vote_set.count()

#this will give the total result count of every choice in dictionary and can be 
#get by using for loop in views.

	def get_result_dict(self):
		res=[]
		for choice in self.choice_set.all():
			d={}
			d['text']= choice.poll
			d['choice']=choice.choice_text
			d['num_votes']= choice.get_vote_count
			if not self.get_vote_count:
				d['percentage']=0
			else:
				d['percentage']=(choice.get_vote_count/self.get_vote_count)*100

			res.append(d)
		return res


	

class Choice(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=250)

	def __str__(self):
		return self.choice_text

	@property
	def get_vote_count(self):
		return self.vote_set.count()
	

class Vote(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	poll= models.ForeignKey(Poll, on_delete=models.CASCADE)
	choice= models.ForeignKey(Choice, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.poll.text[:15]} - {self.choice} - {self.user}'