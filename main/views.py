from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home/index.html")

def event(request):
    return render (request,'home/event.html')