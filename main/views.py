from django.shortcuts import redirect, render
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

def event_view(request, event_slug):
    if(Event.objects.filter(slug=event_slug)):
        eve_obj = Event.objects.get(slug=event_slug)
        context = {'eve_obj':eve_obj}
        return render(request,'home/event_details.html',context)
    else:
        return redirect('event')


def Blog(request):
    blog_obj= blog.objects.all()
    return render(request, "home/blog.html", {'blog_obj':blog_obj})

def blog_view(request,slug):
    if(blog.objects.filter(slug=slug)):
        blogs = blog.objects.get(slug=slug)
        blog_dets = blogDetails.objects.filter(slug=slug)
        context = {'blogs':blogs ,'blog_dets':blog_dets}
        return render(request, 'home/blog-detail.html', context)
    else:
        return redirect('blog')

        

def blog_detail(request,blog_slug, blogdet_slug):
    if (blog.objects.filter(slug=blog_slug)):
        if(blogDetails.objects.filter(slug=blogdet_slug)):
            blog_details = blogDetails.objects.filter(slug=blogdet_slug).first
            context = {'blog_details':blog_details}
            return render(request, "home/blog-detail.html", context)
        else:
            return redirect('blog')

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

def event_details(request):
    return render(request, "home/event_details.html")

def news_detail(request):
    return render(request, "home/news_detail.html")

def voting_detail(request):
    return render(request, "home/voting_detail.html")

