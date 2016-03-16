from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import Page
from django.core.urlresolvers import reverse
from helpers import paginate

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def question(request, id):
	try:
		qst = Question.objects.get(pk=id)
	except Post.DoesNotExist:
		raise Http404
	return render(request, 'tmpl/question.html', {
		'qst': qst,
	})

def questions(request):
	questions = Question.objects.allByDate()
	paginator, page = paginate(request, questions)
	url = reverse('questions')
	return render(request, 'tmpl/questions.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
		'baseurl': url,
	})

def popular(request):
        questions = Question.objects.allByRating()
        paginator, page = paginate(request, questions)
        url = reverse('popular')
        return render(request, 'tmpl/popular.html', {
                'questions': page.object_list,
                'paginator': paginator,
                'page': page,
                'baseurl': url,
        })
