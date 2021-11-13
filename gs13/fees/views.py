from django.shortcuts import render

# Create your views here.
def Fees1(request):
    return render(request, 'fees/feesone.html')

def Fees2(request):
    return render(request, 'fees/feestwo.html')
