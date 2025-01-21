# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("HELLO WORLD! I am Home")
    return render(request,'home.html')

def about(request):
    # return HttpResponse("I am about page")
    return render(request,'about.html')

def info(request):
    return render(request, 'info.html')
