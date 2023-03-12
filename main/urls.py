from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.home, name="home"),  
    path('voting/', views.voting, name="voting"),  
    path('about/', views.about, name="about"),  
    path('company/', views.company, name="company"),  
    path('team/', views.team, name="team"),  
    path('testimonial/', views.testimonial, name="testimonial"),  
    path('event/', views.event, name="event"),  
    path('blog/', views.blog, name="blog"), 
    path('gallery/', views.gallery, name="gallery"),  
    path('news/', views.news, name="news"),  
    path('faq/', views.faq, name="faq"),  
    path('contact/', views.contact, name="contact"),  
    path('login/', views.login, name="login"),  
    path('register/', views.register, name="register"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)