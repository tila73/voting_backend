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
def event_detail(request):
    return render(request, 'admin/event_detail.html')
def news(request):
    return render(request, 'admin/news.html')
def news_detail(request):
    return render(request, 'admin/news_detail.html')

def create_news(request):
    return render(request, 'admin/create_action/create_news.html')

def create_news_details(request):
    return render(request, 'admin/create_action/create_news_detail.html')

def create_event(request):
    return render(request, 'admin/create_action/create_event.html')

def create_event_details(request):
    return render(request, 'admin/create_action/create_event_details.html')

# update

def update_news(request):
    return render(request, 'admin/update_action/update_news.html')

def update_news_detail(request):
    return render(request, 'admin/update_action/update_news_detail.html')

def update_event(request):
    return render(request, 'admin/update_action/update_event.html')

def update_event_detail(request):
    return render(request, 'admin/update_action/update_event_detail.html')
