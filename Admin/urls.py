from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.Dashboard, name="admin_Dashboard"),  
    path('User/', views.Users, name="User"),  
    path('Event', views.adminevent, name="admin_Event"),  
    path('faq/', views.faqq, name="admin_faq"),
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
    path('about/', views.about, name="admin_about"),  
    path('about/detail/', views.about_detail, name="admin_about_detail"),  
    path('blogs/', views.blogs, name="admin_blog"),
    path('blog/detail/', views.blog_detail, name="admin_blog_detail"),  
    path('testimonial', views.testimonial, name="admin_testimonial"),  
    path('testimonial/detail/', views.testimonial_detail, name="admin_testimonial_detail"),  
    
    # create section
    path('user/create/', views.create_user, name="create_user"),  
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
         name="create_about_detail"),
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
    path('company/update/<int:company_id>/', views.update_company, name="update_company"),
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



        #! delete section
        path('news/delete/<int:news_id>/', views.delete_news, name="delete_news"),  
        path('news/delete_detail/<int:id>/', views.delete_news_details, name="delete_news_details"),  
        path('events/delete/<int:id>/', views.delete_event, name="delete_event"),  
        path('events/delete_detail/<int:id>/', views.delete_event_details, name="delete_event_details"),
        path('faq/delete/<int:id>/', views.delete_faq, name="delete_faq"),
        path('services/delete/<int:service_id>/', views.delete_service, name="delete_service"),
        path('teams/delete/<int:id>/', views.delete_team, name="delete_team"),
        path('whychooseus/delete/<int:id>/', views.delete_whychooseus, name="delete_whychooseus"), 
        path('company/delete/<int:id>/', views.delete_company, name="delete_company"),
        path('counts/delete/<int:id>/', views.delete_counts, name="delete_counts"),
        path('gallery/delete/<int:id>/', views.delete_gallery, name="delete_gallery"),
        path('slider/delete/<int:id>/', views.delete_slider, name="delete_slider"),
        
        path('about/delete/<int:id>/', views.delete_about, name="delete_about"),
        path('about/delete_detail/<int:id>/', views.delete_about_details, name="delete_about_detail"),
        path('blog/delete/<int:id>/', views.delete_blog, name="delete_blog"),
        path('blog/delete_detail/<int:id>/', views.delete_blog_details, name="delete_blog_details"),
        path('testimonial/delete/<int:id>/', views.delete_testimonial, name="delete_testimonial"),
        path('testimonial/delete_detail/<int:id>/', views.delete_testimonial_details, name="delete_testimonial_details"),
    
           
     # detail section

    path('User/view/<int:id>/', views.view_Users, name="view_User"),  
    path('Event/view/<int:id>/', views.view_adminevent, name="view_admin_Event"),  
    path('faq/view/<int:id>/', views.view_faqq, name="view_admin_faq"),
    path('teams/view/<int:id>/', views.view_teams, name="view_admin_teams"),
    path('services/view/<int:id>/', views.view_services, name="view_admin_services"),
    path('whychooseus/view/<int:id>/', views.view_whychooseus, name="view_admin_whychooseus"),
    path('Event/detail/view/<int:id>/', views.view_event_detail, name="view_admin_event_detail"),  
    path('news/view/<int:id>/', views.view_news, name="view_admin_news"),  
    path('news/detail/view/<int:id>/', views.view_news_detail, name="view_admin_news_detail"),  
    path('company/view/<int:id>/', views.view_company, name="view_admin_company"),
    path('gallery/view/<int:id>/', views.view_gallery, name="view_admin_gallery"),
    path('slider/view/<int:id>/', views.view_slider, name="view_admin_slider"),
    path('counts/view/<int:id>/', views.view_counts, name="view_admin_counts"),
    path('about/view/<int:id>/', views.view_about, name="view_admin_about"),  
    path('about/detail/view/<int:id>/', views.view_about_detail, name="view_admin_about_detail"),  
    path('blog/view/<int:id>/', views.view_Blog, name="view_admin_blog"),  
    path('blog/detail/view/<int:id>/', views.view_blog_detail, name="view_admin_blog_detail"),  
    path('testimonial/view/<int:id>/', views.view_testimonial, name="view_admin_testimonial"),  
    path('testimonial/detail/view/<int:id>/', views.view_testimonial_detail, name="view_admin_testimonial_detail"),

    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)