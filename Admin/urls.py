from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.Dashboard, name="Dashboard"),  
    path('Event', views.Event, name="Event"),  
    path('Event/details/', views.event_detail, name="event_detail"),  
    path('news/', views.news, name="news"),  
    path('news/details/', views.news_detail, name="news_detail"),  

        # create section
    path('news/create/', views.create_news, name="create_news"),  
    path('news/create_detail/', views.create_news_details, name="create_news_details"),  


# update section
    path('news/update/', views.update_news, name="update_news"),  
    path('news/update_details/', views.update_news_detail, name="update_news_detail"),  

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)