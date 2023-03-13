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
<<<<<<< HEAD


def company(request):
    return render(request, 'admin/company.html')

def gallery(request):
    return render(request, 'admin/gallery.html')

def counts(request):
    return render(request, 'admin/counts.html')

def slider(request):
    return render(request, 'admin/slider.html')


def create_news(request):
    return render(request, 'admin/create_action/create_news.html')

def create_news_details(request):
    return render(request, 'admin/create_action/create_news_detail.html')

# update

def update_news(request):
    return render(request, 'admin/update_action/update_news.html')

def update_news_detail(request):
    return render(request, 'admin/update_action/update_news_detail.html')

=======
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
>>>>>>> a09215e (this is from sujit)
