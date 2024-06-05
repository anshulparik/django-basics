from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World! I am HomePage.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("I am AboutPage.")
    return render(request, 'about.html')