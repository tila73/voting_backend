from django.shortcuts import render

# Create your views here.
def Dashboard(request):
    return render(request, 'admin/admin.html')


def Event(request):
    return render(request, 'admin/event.html')

def faq(request):
    return render(request, 'admin/faq.html')

def teams(request):
    return render(request, 'admin/teams.html')

def services(request):
    return render(request, 'admin/services.html')

def whychooseus(request):
    return render(request, 'admin/whychooseus.html')