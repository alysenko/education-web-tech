from django.http import HttpResponse 

def notfound(request, *args, **kwargs):
	return HttpResponseNotFound()
