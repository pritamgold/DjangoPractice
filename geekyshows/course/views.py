from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learnDjango(request):
    return HttpResponse('Learn Django')

def index(request):
    return HttpResponse('<h1>Home Page</h1>')
