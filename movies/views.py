from django.http import HttpResponse

def index(request):
    return HttpResponse('Home Page')

def movies(request):
    return HttpResponse('Movies View')