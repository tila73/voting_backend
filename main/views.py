from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    event = Event.objects.all()
    slider = Slider.objects.all()
    context = {'event':event, 'slider':slider,}
    return render(request, "home/index.html", context)

def voting(request):
    return render(request, "home/voting.html")

def about(request):
    about = About.objects.all()
    counts = Counts.objects.all()
    testimonial = Testimonial.objects.all()
    context = {'about':about,'counts':counts, 'testimonial':testimonial}
    return render(request, "home/about.html", context)

def company(request):
    company = Company.objects.all()
    services = Service.objects.all()
    whychooseus = WhyChooseUs.objects.all()
    context = {'company':company, 'services':services, 'whychooseus':whychooseus}
    return render(request, "home/company.html", context)

def team(request):
    team = Teams.objects.all()
    team_member = TeamMembers.objects.all()
    context = {'team':team, 'team_member':team_member}
    return render(request, "home/team.html",context)

def testimonial(request):
    testimonial = Testimonial.objects.all()
    context = {'testimonial':testimonial}
    return render(request, "home/testimonial.html", context)

def event(request):
    event_objs = Event.objects.all()
    return render (request,'home/event.html',{'event_objs':event_objs})

def Blog(request):
    blog_objects = blog.objects.all()
    return render(request, "home/blog.html", {'blog': blog_objects})

def gallery(request):
    return render(request, "home/gallery.html")

def news(request):
    news_object = News.objects.all()
    return render(request, "home/news.html", {'news': news_object})

def faq(request):
    return render(request, "home/faq.html")

def contact(request):
    return render(request, "home/contact.html")

def login(request):
    return render(request, "home/login.html")

def register(request):
    return render(request, "home/register.html")

def blog_detail(request):
    blog_detail_object = blogDetails.objects.all()
    return render(request, "home/blog-detail.html", {'blogd': blog_detail_object})

def event_details(request):
    return render(request, "home/event_details.html")

def news_detail(request):
    news_details_object = NewsDetails.objects.all()
    return render(request, "home/news_detail.html", {'newsd': news_details_object})

def voting_detail(request):
    return render(request, "home/voting_detail.html")

