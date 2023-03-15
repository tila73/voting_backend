from django.shortcuts import render, redirect
from .forms import *

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

def company(request):
    company_object = Company.objects.all()
    return render(request, 'admin/company.html', {'company':company_object})

def gallery(request):
    return render(request, 'admin/gallery.html')

def counts(request):
    return render(request, 'admin/counts.html')

def slider(request):
    return render(request, 'admin/slider.html')


def about(request):
    return render(request, 'admin/about.html')


def about_detail(request):
    return render(request, 'admin/about_detail.html')


def blog(request):
    return render(request, 'admin/blog.html')


def blog_detail(request):
    return render(request, 'admin/blog_detail.html')


def testimonial(request):
    return render(request, 'admin/testimonial.html')


def testimonial_detail(request):
    return render(request, 'admin/testimonial_detail.html')

# Create
def create_news(request):
    if request.method == "GET":
        news = NewsForm
        return render(request, 'admin/create_action/create_news.html', context={'form': news})
    else:
        news = NewsForm(request.POST, request.FILES)
        if news.is_valid():
            news.save()
            return redirect('admin_news')
    return render(request, 'admin/create_action/create_news.html', context={'form': news})

def create_news_details(request):
    if request.method == "GET":
        news_detail = NewsDetailsForm
        return render(request, 'admin/create_action/create_news_detail.html', context={'form': news_detail})
    else:
        news_detail = NewsDetailsForm(request.POST, request.FILES)
        if news_detail.is_valid():
            news_detail.save()
            return redirect('admin_news_detail')
    return render(request, 'admin/create_action/create_news_detail.html')

def create_event(request):
    if request.method == "GET":
        event = EventForm
        return render(request, 'admin/create_action/create_event.html', context={'form': event})
    else:
        event = EventForm(request.POST, request.FILES)
        if event.is_valid():
            event.save()
            return redirect('admin_Event')
    return render(request, 'admin/create_action/create_event.html', context={'form': event})

def create_event_details(request):
    if request.method == "GET":
        event_details = EventDetailsForm
        return render(request, 'admin/create_action/create_event_details.html', context={'form': event_details})
    else:
        event_details = EventDetailsForm(request.POST, request.FILES)
        if event_details.is_valid():
            event_details.save()
            return redirect('admin_event_detail')
    return render(request, 'admin/create_action/create_event_details.html', context={'form': event_details})

def create_faq(request):
    if request.method == "GET":
        faq = faqForm
        return render(request, 'admin/create_action/create_faq.html', context={'form': faq})
    else:
        faq = faqForm(request.POST, request.FILES)
        if faq.is_valid():
            faq.save()
            return redirect('admin_faq')
    return render(request, 'admin/create_action/create_faq.html', context={'form': faq})

def create_service(request):
    if request.method == "GET":
        service = ServiceForm
        return render(request, 'admin/create_action/create_service.html', context={'form': service})
    else:
        service = ServiceForm(request.POST, request.FILES)
        if service.is_valid():
            service.save()
            return redirect('admin_service')
    return render(request, 'admin/create_action/create_service.html', context={'form': service})

def create_team(request):
    if request.method == "GET":
        team = TeamsForm
        return render(request, 'admin/create_action/create_team.html', context={'form': team})
    else:
        team = TeamsForm(request.POST, request.FILES)
        if team.is_valid():
            team.save()
            return redirect('admin_team')
    return render(request, 'admin/create_action/create_team.html', context={'form': team})

def create_whychooseus(request):
    if request.method == "GET":
        whychooseus_form = WhyChooseUsForm
        return render(request, 'admin/create_action/create_whychooseus.html', context={'form': whychooseus_form})
    else:
        whychooseus_form = WhyChooseUsForm(request.POST, request.FILES)
        if whychooseus_form.is_valid():
            whychooseus_form.save()
            return redirect('admin_whychooseus')
    return render(request, 'admin/create_action/create_whychooseus.html', context={'form': whychooseus_form})


def create_company(request):
    if request.method=="GET":
        company_form = CompanyForm
        return render(request, 'admin/create_action/create_company.html', context={'form':company_form})
    else:
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company_form.save()
            return redirect('admin_company')
    return render(request, 'admin/create_action/create_company.html', context={'form':company_form})

def create_counts(request):
    if request.method == "GET":
        counts_form = CountsForm
        return render(request, 'admin/create_action/create_counts.html', context={'form': counts_form})
    else:
        counts_form = CountsForm(request.POST, request.FILES)
        if counts_form.is_valid():
            counts_form.save()
            return redirect('admin_counts')
    return render(request, 'admin/create_action/create_counts.html', context= {'form':counts_form})


def create_gallery(request):
    if request.method == "GET":
        gallery_form = GalleryForm
        return render(request, 'admin/create_action/create_gallery.html', context={'form': gallery_form})
    else:
        gallery_form = GalleryForm(request.POST, request.FILES)
        if gallery_form.is_valid():
            gallery_form.save()
            return redirect('admin_gallery')
    return render(request, 'admin/create_action/create_gallery.html', context={'form': gallery_form})


def create_slider(request):
    if request.method == "GET":
        slider_form = SliderForm
        return render(request, 'admin/create_action/create_slider.html', context={'form': slider_form})
    else:
        slider_form = SliderForm(request.POST, request.FILES)
        if slider_form.is_valid():
            slider_form.save()
            return redirect('admin_slider')
    return render(request, 'admin/create_action/create_slider.html', context={'form': slider_form})

# sujit create wala


def create_about(request):
    if request.method == "GET":
        create_about = AboutForm
        return render(request, 'admin/create_action/create_about.html', context={'form': create_about})
    else:
        create_about = AboutForm(request.POST, request.FILES)
        if create_about.is_valid():
            create_about.save()
            return redirect('admin_about')
    return render(request, 'admin/create_action/create_about.html', context={'form': create_about})


def create_about_details(request):
    return render(request, 'admin/create_action/create_about_detail.html')


def create_blog(request):
    return render(request, 'admin/create_action/create_blog.html')


def create_blog_details(request):
    return render(request, 'admin/create_action/create_blog_detail.html')


def create_testimonial(request):
    return render(request, 'admin/create_action/create_testimonial.html')


def create_testimonial_details(request):
    return render(request, 'admin/create_action/create_testimonial_detail.html')


# update
def update_news(request):
    return render(request, 'admin/update_action/update_news.html')

def update_news_detail(request):
    return render(request, 'admin/update_action/update_news_detail.html')

def update_event(request):
    return render(request, 'admin/update_action/update_event.html')

def update_event_detail(request):
    return render(request, 'admin/update_action/update_event_detail.html')

def update_faq(request):
    return render(request, 'admin/update_action/update_faq.html')

def update_team(request):
    return render(request, 'admin/update_action/update_team.html')

def update_service(request):
    return render(request, 'admin/update_action/update_service.html')

def update_whychooseus(request):
    return render(request, 'admin/update_action/update_whychooseus.html')


def update_company(request):
    return render(request, 'admin/update_action/update_company.html')


def update_counts(request):
    return render(request, 'admin/update_action/update_counts.html')


def update_gallery(request):
    return render(request, 'admin/update_action/update_gallery.html')


def update_slider(request):
    return render(request, 'admin/update_action/update_slider.html')

# sujit update wala


def update_about(request):
    return render(request, 'admin/update_action/update_about.html')


def update_about_detail(request):
    return render(request, 'admin/update_action/update_about_detail.html')


def update_blog(request):
    return render(request, 'admin/update_action/update_blog.html')


def update_blog_detail(request):
    return render(request, 'admin/update_action/update_blog_detail.html')


def update_testimonial(request):
    return render(request, 'admin/update_action/update_testimonial.html')


def update_testimonial_detail(request):
    return render(request, 'admin/update_action/update_testimonial_detail.html')
