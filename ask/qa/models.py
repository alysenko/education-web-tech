from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
	def allByDate(self):
		return self.orderby('-added_at')

	def allByRating(self):
		return self.orderby('-rating')

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name='questions')
	likes = models.ManyToManyField(User, related_name='likes')

	objects = QuestionManager()

	def url(self):
		return reverse('question', kwargs={'id': self.id})

#	def __str__(self):
	def __unicode__(self):
		return self.title


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User, related_name='answers')
