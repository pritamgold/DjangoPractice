from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cours_one(request):
    return render(request, 'course1.html')

def course_two(request):
    return render(request, 'course2.html')