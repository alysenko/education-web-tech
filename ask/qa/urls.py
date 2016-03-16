#/ask/qa/urls.py

from django.conf.urls import url
from qa.views import test
from qa.views import question
from qa.views import questions
from qa.views import popular

urlpatterns = [
	url(r'^$', questions, name='home'),
	url(r'^login/', test, name='login'),
	url(r'^signup/', test, name='signup'),
	url(r'^question/(?P<id>\d+)/$', question, name='question'),
	url(r'^ask/', test, name='ask'),
	url(r'^popular/', popular, name='popular'),
	url(r'^new/', test, name='new'),
]
