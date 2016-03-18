#/ask/qa/urls.py

from django.conf.urls import url
from qa.views import test
from qa.views import popular, questions
from qa.views import question 
from qa.views import ask, answer
from qa.views import signup, login

urlpatterns = [
	url(r'^$', questions, name='home'),
	url(r'^login/', login, name='login'),
	url(r'^signup/', signup, name='signup'),
	url(r'^question/(?P<id>\d+)/$', question, name='question'),
	url(r'^ask/$', ask, name='ask'),
	url(r'^answer/$', answer, name='answer'),
	url(r'^popular/', popular, name='popular'),
]
