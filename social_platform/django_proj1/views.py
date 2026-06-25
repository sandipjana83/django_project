from django.http import HttpResponse
from django.shortcuts import render
def Home(request):
    # return  HttpResponse("Hello,Welcome to My home Pages")
    return render(request,'index.html')

def About(request):
    return  HttpResponse("Hello,Welcome to My about Pages")

def Contact(request):
    return  HttpResponse("Hello,Welcome to My contact Pages")