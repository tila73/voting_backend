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

        # create section
    path('news/create/', views.create_news, name="create_news"),  
    path('news/create_detail/', views.create_news_details, name="create_news_details"),  
    path('events/create/', views.create_event, name="create_event"),  
    path('events/create_detail/', views.create_event_details, name="create_event_details"),  


# update section
    path('news/update/', views.update_news, name="update_news"),  
    path('news/update_details/', views.update_news_detail, name="update_news_detail"),  
    path('events/update/', views.update_event, name="update_event"),  
    path('events/update_details/', views.update_event_detail, name="update_event_detail"),  

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)