#from django.shortcuts import render

from django.http import HttpResponse

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def question(request, id):
	return HttpResponse('OK')

def questions(request, *args):
	return HttpResponse('OK')
