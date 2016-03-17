from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.paginator import Page
from django.core.urlresolvers import reverse
from helpers import paginate
from models import Question, Answer
import forms

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def question(request, id):
	try:
		qst = Question.objects.get(pk=id)
	except Question.DoesNotExist:
		raise Http404
	answers = Answer.objects.filter(question=qst)
	answers = answers[:]
	form = forms.AnswerForm(initial={'question_id': id})
	return render(request, 'question.html', {
		'qst': qst,
		'answers': answers,
		'form': form,
	})

def questions(request):
	questions = Question.objects.allByDate()
	paginator, page = paginate(request, questions)
	url = reverse('home')
	return render(request, 'questions.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
		'baseurl': url,
	})

def popular(request):
        questions = Question.objects.allByRating()
        paginator, page = paginate(request, questions)
        url = reverse('popular')
        return render(request, 'popular.html', {
                'questions': page.object_list,
                'paginator': paginator,
                'page': page,
                'baseurl': url,
        })

def ask(request):
	if request.method == "GET":
		form = forms.AskForm()
	elif request.method == "POST":
		form = forms.AskForm(request.POST)
		if form.is_valid():
			qst = form.save()
			url = qst.url()
			return HttpResponseRedirect(url)
	return render(request, 'ask.html', { 'form': form, })
#	else:
#		raise Http404

def answer(request):
	if request.method == "POST":
		form = forms.AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save()
			url = answer.question.url()
			return HttpResponseRedirect(url)
		else:
			id = form.data['question_id']
			url = reverse('question', kwargs={'id': id})
			return HttpResponseRedirect(url)
	else:
		raise Http404
