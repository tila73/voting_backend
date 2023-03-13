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
    path('company/', views.company, name="company"),
    path('gallery/', views.gallery, name="gallery"),
    path('slider/', views.slider, name="slider"),
    path('counts/', views.counts, name="counts"),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)