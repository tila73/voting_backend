from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def Dashboard(request):
    return render(request, 'admin/admin.html')

def Users(request):
    users = User.objects.all()
    return render(request, 'admin/user.html', {'users':users})


def adminevent(request):
    event_object = Event.objects.all()
    return render(request, 'admin/event.html',{'event': event_object})

def faqq(request):
    faq_object = faq.objects.all()
    return render(request, 'admin/faq.html', {'faq':faq_object})

def teams(request):
    team_object = Teams.objects.all()
    return render(request, 'admin/teams.html',{'teams': team_object})

def services(request):
    service_objects = Service.objects.all()
    return render(request, 'admin/services.html',{'services': service_objects})

def whychooseus(request):
    whychooseus_object = WhyChooseUs.objects.all()
    return render(request, 'admin/whychooseus.html',{'whychooseus': whychooseus_object})
def event_detail(request):
    event_details_object = EventDetails.objects.all()
    return render(request, 'admin/event_detail.html',{'eventd': event_details_object})
def news(request):
    news_object = News.objects.all()
    return render(request, 'admin/news.html', {'news': news_object})
def news_detail(request):
    news_detail_object = NewsDetails.objects.all()
    return render(request, 'admin/news_detail.html',{'newsd': news_detail_object})

def company(request):
    company_object = Company.objects.all()
    return render(request, 'admin/company.html', {'company':company_object})

def gallery(request):
    gallery_object = Gallery.objects.all()
    return render(request, 'admin/gallery.html', {'gallery': gallery_object})

def counts(request):
    count_object = Counts.objects.all()
    return render(request, 'admin/counts.html', {'counts': count_object})

def slider(request):
    slider_object = Slider.objects.all()
    return render(request, 'admin/slider.html', {'slider': slider_object})


def about(request):
    about_object = About.objects.all()
    return render(request, 'admin/about.html', {'about': about_object})


def about_detail(request):
    about_detail_object = AboutDetails.objects.all()
    return render(request, 'admin/about_detail.html', {'aboutd': about_detail_object})

def blogs(request):
    blog_obj = blog.objects.all()
    return render(request, 'admin/blog.html', {'blog_obj': blog_obj})


def blog_detail(request):
    blog_detail_objects = blogDetails.objects.all()
    return render(request, 'admin/blog_detail.html',{'blogd': blog_detail_objects})


def testimonial(request):
    testimonial_object = Testimonial.objects.all()
    return render(request, 'admin/testimonial.html',{'testimonial': testimonial_object})


def testimonial_detail(request):
    testimonial_detail_object = TestimonialDetails.objects.all()
    return render(request, 'admin/testimonial_detail.html', {'testimoniald': testimonial_detail_object})

# Create
def create_user(request):
    if request.method == "GET":
        users = UserForm
        return render(request, 'admin/create_action/create_user.html', context={'form': users})
    else:
        users = UserForm(request.POST, request.FILES)
        if users.is_valid():
            users.save()
            return redirect('User')
    return render(request, 'admin/create_action/create_user.html', context={'form': users})


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
            return redirect('admin_services')
    return render(request, 'admin/create_action/create_service.html', context={'form': service})

def create_team(request):
    if request.method == "GET":
        team = TeamsForm
        return render(request, 'admin/create_action/create_team.html', context={'form': team})
    else:
        team = TeamsForm(request.POST, request.FILES)
        if team.is_valid():
            team.save()
            return redirect('admin_teams')
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
    if request.method == "GET":
        create_about_details = AboutDetailsForm
        return render(request, 'admin/create_action/create_about_detail.html', context={'form': create_about_details})
    else:
        create_about_details = AboutDetailsForm(request.POST, request.FILES)
        if create_about_details.is_valid():
            create_about_details.save()
            return redirect('admin_about_detail')
    return render(request, 'admin/create_action/create_about_detail.html', context={'form': create_about_details})


def create_blog(request):
    if request.method == "GET":
        create_blogs = blogForm
        return render(request, 'admin/create_action/create_blog.html', context={'form': create_blogs})
    else:
        create_blogs = blogForm(request.POST, request.FILES)
        if create_blogs.is_valid():
            create_blogs.save()
            return redirect('admin_blog')
    return render(request, 'admin/create_action/create_blog.html', context={'form': create_blogs})


def create_blog_details(request):
    if request.method == "GET":
        create_blog_details = blogDetailsForm
        return render(request, 'admin/create_action/create_blog_detail.html', context={'form': create_blog_details})
    else:
        create_blog_details = blogDetailsForm(request.POST, request.FILES)
        if create_blog_details.is_valid():
            create_blog_details.save()
            return redirect('admin_blog_detail')
    return render(request, 'admin/create_action/create_blog_detail.html', context={'form': create_blog_details})


def create_testimonial(request):
    if request.method == "GET":
        create_testimonial = TestimonialForm
        return render(request, 'admin/create_action/create_testimonial.html', context={'form': create_testimonial})
    else:
        create_testimonial = TestimonialForm(request.POST, request.FILES)
        if create_testimonial.is_valid():
            create_testimonial.save()
            return redirect('admin_testimonial')
    return render(request, 'admin/create_action/create_testimonial.html', context={'form': create_testimonial})


def create_testimonial_details(request):
    if request.method == "GET":
        create_testimonial_details = TestimonialDetailsForm
        return render(request, 'admin/create_action/create_testimonial_detail.html', context={'form': create_testimonial_details})
    else:
        create_testimonial_details = TestimonialDetailsForm(request.POST, request.FILES)
        if create_testimonial_details.is_valid():
            create_testimonial_details.save()
            return redirect('admin_testimonial_detail')
    return render(request, 'admin/create_action/create_testimonial_detail.html', context={'form': create_testimonial_details})


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



#delete
def delete_news(request, news_id):
    newsobj = News.objects.get(id=news_id)
    if request.method=="POST":
        newsobj.delete()
        return redirect('admin_news')



def delete_news_details(request, id):
    obj = NewsDetails.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_news_detail')


def delete_event(request, id):
    obj = Event.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_Event')



def delete_event_details(request, id):
    obj = EventDetails.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_event_detail')



def delete_faq(request, id):
    obj = faq.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_faq')



def delete_service(request, service_id):
    obj = Service.objects.get(id=service_id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_services')



def delete_team(request, id):
    obj = Teams.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_teams')



def delete_whychooseus(request, id):
    obj = WhyChooseUs.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_whychooseus')




def delete_company(request, id):
    obj = Company.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_company')



def delete_counts(request, id):
    obj = Counts.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_counts')




def delete_gallery(request, id):
    obj = Gallery.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_gallery')




def delete_slider(request, id):
    obj = Slider.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_slider')


def delete_about(request, id):
    obj = About.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_about')


def delete_about_details(request,id):
    obj = AboutDetails.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_about_detail')


def delete_blog(request,id):    
    obj = blog.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_blog')


def delete_blog_details(request,id):
    obj = blogDetails.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_blog_detail')


def delete_testimonial(request,id):
    obj = Testimonial.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_testimonial')


def delete_testimonial_details(request,id):
    obj = TestimonialDetails.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('admin_testimonial_detail')

# detail views

def view_Users(request,id):
    users = User.objects.get(id=id)
    return render(request, 'admin/view_action/view_user.html', {'users':users})


def view_adminevent(request,id):
    event_object = Event.objects.get(id=id)
    return render(request, 'admin/view_action/view_event.html',{'event': event_object})

def view_faqq(request,id):
    faq_object = faq.objects.get(id=id)
    return render(request, 'admin/view_action/view_faq.html', {'faq':faq_object})

def view_teams(request,id):
    team_object = Teams.objects.get(id=id)
    return render(request, 'admin/view_action/view_teams.html',{'teams': team_object})

def view_services(request,id):
    service_objects = Service.objects.get(id=id)
    return render(request, 'admin/view_action/view_services.html',{'services': service_objects})

def view_whychooseus(request,id):
    whychooseus_object = WhyChooseUs.objects.get(id=id)
    return render(request, 'admin/view_action/view_whychooseus.html',{'whychooseus': whychooseus_object})

def view_event_detail(request,id):
    event_details_object = EventDetails.objects.get(id=id)
    return render(request, 'admin/view_action/view_event_detail.html',{'eventd': event_details_object})

def view_news(request,id):
    news_object = News.objects.get(id=id)
    return render(request, 'admin/view_action/view_news.html', {'news': news_object})

def view_news_detail(request,id):
    news_detail_object = NewsDetails.objects.get(id=id)
    return render(request, 'admin/view_action/view_news_detail.html',{'newsd': news_detail_object})

def view_company(request,id):
    company_object = Company.objects.get(id=id)
    return render(request, 'admin/view_action/view_company.html', {'company':company_object})

def view_gallery(request,id):
    gallery_object = Gallery.objects.get(id=id)
    return render(request, 'admin/view_action/view_gallery.html', {'gallery': gallery_object})

def view_counts(request,id):
    count_object = Counts.objects.get(id=id)
    return render(request, 'admin/view_action/view_counts.html', {'counts': count_object})

def view_slider(request,id):
    slider_object = Slider.objects.get(id=id)
    return render(request, 'admin/view_action/view_slider.html', {'slider': slider_object})


def view_about(request,id):
    about_object = About.objects.get(id=id)
    return render(request, 'admin/view_action/view_about.html', {'about': about_object})


def view_about_detail(request,id):
    about_detail_object = AboutDetails.objects.get(id=id)
    return render(request, 'admin/view_action/view_about_detail.html', {'aboutd': about_detail_object})


def view_Blog(request,id):
    blog_object = blog.objects.get(id=id)
    return render(request, 'admin/view_action/view_blog.html', {'blog': blog_object})


def view_blog_detail(request,id):
    blog_detail_objects = blogDetails.objects.get(id=id)
    return render(request, 'admin/view_action/view_blog_detail.html',{'blogd': blog_detail_objects})


def view_testimonial(request,id):
    testimonial_object = Testimonial.objects.get(id=id)
    return render(request, 'admin/view_action/view_testimonial.html',{'testimonial': testimonial_object})


def view_testimonial_detail(request):
    testimonial_detail_object = TestimonialDetails.objects.get(id=id)
    return render(request, 'admin/view_action/view_testimonial_detail.html', {'testimoniald': testimonial_detail_object})





# ! details section



