from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fees_one(request):
    return render(request, 'fees1.html')

def fees_two(request):
    return HttpResponse(request, 'fees2.html')