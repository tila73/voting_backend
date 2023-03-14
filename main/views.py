from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home/index.html")

def voting(request):
    return render(request, "home/voting.html")

def about(request):
    return render(request, "home/about.html")

def company(request):
    return render(request, "home/company.html")

def team(request):
    return render(request, "home/team.html")

def testimonial(request):
    return render(request, "home/testimonial.html")

def event(request):
    return render (request,'home/event.html')

def blog(request):
    return render(request, "home/blog.html")

def gallery(request):
    return render(request, "home/gallery.html")

def news(request):
    return render(request, "home/news.html")

def faq(request):
    return render(request, "home/faq.html")

def contact(request):
    return render(request, "home/contact.html")

def login(request):
    return render(request, "home/login.html")

def register(request):
    return render(request, "home/register.html")

def blog_detail(request):
    return render(request, "home/blog-detail.html")

def event_details(request):
    return render(request, "home/event_details.html")

def news_detail(request):
    return render(request, "home/news_detail.html")

def voting_detail(request):
    return render(request, "home/voting_detail.html")

