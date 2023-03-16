from django.shortcuts import render

# Create your views here.

def haii(request):
    return render(request,'haii.html')

def bye(request):
    return render(request,'bye.html')
