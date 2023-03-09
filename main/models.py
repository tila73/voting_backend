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
    about_description = models.TextField(("Description"), max_length=255)
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
class Company(models.Model):
    companyImg = models.ImageField(upload_to='img/', blank=False, null=False)
    title = models.CharField(max_length=150)
    desc = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.title
    
class Service(models.Model):
    servicesImg = models.ImageField(upload_to='img/services', blank=False, null=False)
    title = models.CharField(max_length=150)
    desc = models.TextField()
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.title
    
class WhyChooseUs(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to='img/', blank=False, null=False)
    desc = models.TextField()
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.title
    
class Teams(models.Model):
    title = models.CharField(max_length=150)
    sub_desc = models.TextField()
    img = models.ImageField(upload_to='img/teams', blank=False, null=False)
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.title
