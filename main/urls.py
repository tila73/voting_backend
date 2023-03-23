from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.home, name="home"),  
    path('voting/<int:id>/', views.business_candidate, name="voting"),  
    path('about/', views.about, name="about"),  
    path('company/', views.company, name="company"),  
    path('team/', views.team, name="team"),  
    path('testimonial/', views.testimonial, name="testimonial"),  
    path('event/', views.event, name="event"),  
    path('event/<str:event_slug>/', views.event_view, name="event_view"),  
    path('blog/', views.Blog, name="blog"), 

    path('blog/<str:slug>/',views.blog_view, name="blog_view"),

    path('gallery/', views.gallery, name="gallery"),  
    path('news/', views.news, name="news"),  
    path('faq/', views.faqq, name="faq"),  
    path('contact/', views.contact, name="contact"),  
    path('login/', views.login, name="login"),  
    path('register/', views.register, name="register"),
    path('blog/blog_detail/', views.blog_detail, name="blog_detail"),
    path('event/event_details/', views.event_details, name="event_details"),
    path('news/news_detail/<str:slug>/', views.news_detail, name="news_detail"),
    path('voting/<int:business_id>/<int:candidate_id>/', views.voting_detail, name="voting_detail"),
    path('payment/check/', views.payment),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)