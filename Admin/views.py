from django.shortcuts import render,redirect
from main.models import *
# Create your views here.
def Dashboard(request):
    return render(request, 'admin/admin.html')


def Event(request):
    return render(request, 'admin/event.html')
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

# update

def update_news(request):
    return render(request, 'admin/update_action/update_news.html')

def update_news_detail(request):
    return render(request, 'admin/update_action/update_news_detail.html')

# delete
def delete(request, id):
    request(delete)
    return render(request, 'admin/update_action/update_news_detail.html')

def delete_news(request,news_id):
    news = News.objects.get(id=news_id)
    context = {'news':news}
    if request.method == "POST":
        news.delete()
        return redirect ('news')
