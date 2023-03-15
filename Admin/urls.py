from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.Dashboard, name="admin_Dashboard"),  
    path('Event', views.Event, name="admin_Event"),  
    path('faq/', views.faq, name="admin_faq"),
    path('teams/', views.teams, name="admin_teams"),
    path('services/', views.services, name="admin_services"),
    path('whychooseus/', views.whychooseus, name="admin_whychooseus"),
    path('Event/details/', views.event_detail, name="admin_event_detail"),  
    path('news/', views.news, name="admin_news"),  
    path('news/details/', views.news_detail, name="admin_news_detail"),  

    #nikita
    path('company/', views.company, name="admin_company"),
    path('gallery/', views.gallery, name="admin_gallery"),
    path('slider/', views.slider, name="admin_slider"),
    path('counts/', views.counts, name="admin_counts"),

    #sujit
    path('about', views.about, name="admin_about"),  
    path('about/detail/', views.about_detail, name="admin_about_detail"),  
    path('blog', views.blog, name="admin_blog"),  
    path('blog/detail/', views.blog_detail, name="admin_blog_detail"),  
    path('testimonial', views.testimonial, name="admin_testimonial"),  
    path('testimonial/detail/', views.testimonial_detail, name="admin_testimonial_detail"),  
    
    # create section
    path('news/create/', views.create_news, name="create_news"),  
    path('news/create_detail/', views.create_news_details, name="create_news_details"),  
    path('events/create/', views.create_event, name="create_event"),  
    path('events/create_detail/', views.create_event_details, name="create_event_details"),
    path('faq/create/', views.create_faq, name="create_faq"),
    path('services/create/', views.create_service, name="create_service"),
    path('teams/create/', views.create_team, name="create_team"),
    path('whychooseus/create/', views.create_whychooseus, name="create_whychooseus"), 
    path('company/create/', views.create_company, name="create_company"),
    path('counts/create/', views.create_counts, name="create_counts"),
    path('gallery/create/', views.create_gallery, name="create_gallery"),
    path('slider/create/', views.create_slider, name="create_slider"),
    # .  sujit create walako
    path('about/create/', views.create_about, name="create_about"),
    path('about/create_detail/', views.create_about_details,
         name="create_about_details"),
    path('blog/create/', views.create_blog, name="create_blog"),
    path('blog/create_detail/', views.create_blog_details,
         name="create_blog_details"),
    path('testimonial/create/', views.create_testimonial,
         name="create_testimonial"),
    path('testimonial/create_detail/', views.create_testimonial_details,
         name="create_testimonial_details"),


# update section
    path('news/update/', views.update_news, name="update_news"),  
    path('news/update_details/', views.update_news_detail, name="update_news_detail"),  
    path('events/update/', views.update_event, name="update_event"),  
    path('events/update_details/', views.update_event_detail, name="update_event_detail"), 
    path('company/update/', views.update_company, name="update_company"),
    path('counts/update/', views.update_counts, name="update_counts"),
    path('gallery/update/', views.update_gallery, name="update_gallery"),
    path('slider/update/', views.update_slider, name="update_slider"),
    path('events/update_details/', views.update_event_detail, name="update_event_detail"),
    path('faq/update/', views.update_faq, name="update_faq"),  
    path('services/update/', views.update_service, name="update_service"),  
    path('whychooseus/update/', views.update_whychooseus, name="update_whychooseus"),  
    path('teams/update/', views.update_team, name="update_team"),  
    # sujit update walla ko
    path('about/update/', views.update_about, name="update_about"),
    path('about/update_details/', views.update_about_detail,
         name="update_about_detail"),
    path('blog/update/', views.update_blog, name="update_blog"),
    path('blog/update_details/', views.update_blog_detail,
         name="update_blog_detail"),
    path('testimonial/update/', views.update_testimonial,
         name="update_testimonial"),
    path('testimonial/update_details/', views.update_testimonial_detail,
         name="update_testimonial_detail"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)