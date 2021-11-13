from django.shortcuts import render

# Create your views here.
def Course1(request):
    return render(request, 'course/courseone.html')

def Course2(request):
    return render(request, 'course/coursetwo.html')
