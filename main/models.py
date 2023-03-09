from django.db import models

# Create your models here.
# model for event and event detail page
class Event(models.Model):
    event_title = models.CharField(("Title"), max_length=50)
    event_description =models.TextField(("Description"), max_length=None)
    event_date = models.DateTimeField(("Date"), auto_now=False, auto_now_add=False)
    event_img = models.ImageField(("Image"), upload_to='img/event/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField((""))

    def __str__(self):
       return self.event_title
    


 # model for News and News detail page   
class News(models.Model):
    news_title = models.CharField(("Title"), max_length=50)
    news_description =models.TextField(("Description"))
    news_author = models.CharField(("Written By"), max_length=50)
    news_date = models.DateTimeField(("News date"), auto_now=False, auto_now_add=False)
    news_img = models.ImageField(("Image"), upload_to='img/news/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField()

    def __str__(self):
       return self.news_title
   


# Model for SLider
class Slider(models.Model):
    slider_title = models.CharField(("Title"), max_length=50)
    slider_description = models.TextField(("Description"), max_length=255)
    slider_img = models.ImageField(("Image"), upload_to='img/slider/', height_field=None, width_field=None, max_length=None)
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.slider_title



# About Model
class About(models.Model):
    about_title = models.CharField(("Title"), max_length=50)
    about_description = models.TextField(("Description"), max_length=500)
    about_img = models.ImageField(("Image"), upload_to='img/about/', height_field=None, width_field=None, max_length=None)
    status = models.BooleanField( default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.about_title


# Counts model 
class Counts(models.Model):
    count_number = models.PositiveIntegerField(("Count Number"))
    count_title = models.CharField(("Title"), max_length=50)

    def __str__(self):
        return self.count_title


# Testimonials Model
class Testimonial(models.Model):
    testmoni_name = models.CharField(("Name"), max_length=50)
    testmoni_designation = models.CharField(("Designation"), max_length=30)
    testmoni_message = models.TextField(("Message"))
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.testmoni_name