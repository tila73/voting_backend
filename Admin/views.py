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

def company(request):
    return render(request, 'admin/company.html')

def gallery(request):
    return render(request, 'admin/gallery.html')

def counts(request):
    return render(request, 'admin/counts.html')

def slider(request):
    return render(request, 'admin/slider.html')

# Create
def create_news(request):
    return render(request, 'admin/create_action/create_news.html')

def create_news_details(request):
    return render(request, 'admin/create_action/create_news_detail.html')

def create_event(request):
    return render(request, 'admin/create_action/create_event.html')

def create_event_details(request):
    return render(request, 'admin/create_action/create_event_details.html')

def create_faq(request):
    return render(request, 'admin/create_action/create_faq.html')

def create_service(request):
    return render(request, 'admin/create_action/create_service.html')

def create_team(request):
    return render(request, 'admin/create_action/create_team.html')

def create_whychooseus(request):
    return render(request, 'admin/create_action/create_whychooseus.html')


def create_company(request):
    return render(request, 'admin/create_action/create_company.html')


def create_counts(request):
    return render(request, 'admin/create_action/create_counts.html')


def create_gallery(request):
    return render(request, 'admin/create_action/create_gallery.html')


def create_slider(request):
    return render(request, 'admin/create_action/create_slider.html')

#Sujit
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
