from django.http import HttpResponseNotFound

def notfound(request):
	return HttpResponseNotFound()
