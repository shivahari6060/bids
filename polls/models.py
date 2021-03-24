from django.db import models

from django.conf import settings

# Create your models here.

class Poll(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text= models.CharField(max_length= 250)
	pub_date= models.DateTimeField(auto_now_add=True)
	active= models.BooleanField(default=False)

	def __str__(self):
		return self.text

class Choice(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=250)

	def __str__(self):
		return self.choice_text

class Vote(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	poll= models.ForeignKey(Poll, on_delete=models.CASCADE)
	choice= models.ForeignKey(Choice, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.poll.text[:15]} - {self.choice} - {self.user}'