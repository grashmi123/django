from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!")

def businfo(request):
	return HttpResponse("hii ")
	

		
