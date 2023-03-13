from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.Dashboard, name="Dashboard"),  
    path('Event', views.Event, name="Event"),  
    path('faq/', views.faq, name="faq"),
    path('teams/', views.teams, name="teams"),
    path('services/', views.services, name="services"),
    path('whychooseus/', views.whychooseus, name="whychooseus"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)