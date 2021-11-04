from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course1(req):
    return render(req, 'course1.html')
