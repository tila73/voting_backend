from django.shortcuts import render

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

def company(request):
    return render(request, 'admin/company.html')

def gallery(request):
    return render(request, 'admin/gallery.html')

def counts(request):
    return render(request, 'admin/counts.html')

def slider(request):
    return render(request, 'admin/slider.html')