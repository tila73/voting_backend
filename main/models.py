from django.db import models
# from django.contrib.auth.models import BaseAbstractUser
# form auto generating username 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
# for encrypting password with hash algorithm
from django.contrib.auth.hashers import make_password


# Create your models here.
# model for event and event detail page
class Event(models.Model):
    event_title = models.CharField(("Title"), max_length=100)
    event_description =models.TextField(("Description"), max_length=None)
    event_date = models.DateTimeField(("Date"), auto_now=False, auto_now_add=False)
    event_img = models.ImageField(("Image"), upload_to='img/event/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField((""))

    def __str__(self):
       return self.event_title
    


 # model for News and News detail page   
class News(models.Model):
    news_title = models.CharField(("Title"), max_length=5100)
    news_description =models.TextField(("Description"))
    news_author = models.CharField(("Written By"), max_length=50)
    news_date = models.DateTimeField(("News date"), auto_now=False, auto_now_add=False)
    news_img = models.ImageField(("Image"), upload_to='img/news/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField()

    def __str__(self):
       return self.news_title
   


# Model for SLider
class Slider(models.Model):
    slider_title = models.CharField(("Title"), max_length=100)
    slider_description = models.TextField(("Description"), max_length=255)
    slider_img = models.ImageField(("Image"), upload_to='img/slider/', height_field=None, width_field=None, max_length=None)
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.slider_title



# About Model
class About(models.Model):
    about_title = models.CharField(("Title"), max_length=100)
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
    name = models.CharField(max_length=60)
    post = models.CharField(max_length=100)
    fb_link = models.CharField(max_length=150)
    twitter_link = models.CharField(max_length=150)
    insta_link = models.CharField(max_length=150)
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.title







# # for hashed password
raw_password = 'Insert password12'
hashed_password = make_password(raw_password)

class AdminUser(models.Model):
    name = models.CharField(("Name"), max_length=255)
    username = models.CharField(("Username"), max_length=255, unique=True)
    email = models.EmailField(("Email"), max_length=255, unique=True)
    password = models.CharField(("Password"), max_length=128, default=hashed_password)
    address = models.CharField(("Address"), max_length=100, null=True)
    phone_number = models.CharField(("Phone Number"), max_length=100)
    esewa_number = models.CharField(("Esewa Number"), max_length=100, null=True)
    role = models.IntegerField(("User Role"), default=1, help_text="0=business user(owner), 1=admin, 2=sub business user(owner)")
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active" )
    created_at = models.DateTimeField(("Created date"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated Date"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name



# def generate_username(instance):
#     username = slugify(instance.name)
#     counter = 1
#     while instance.__class__.objects.filter(username=username).exists():
#         username = f'{username}-{counter}'
#         counter += 1
#         return username
    


# @receiver(pre_save, sender=AdminUser)
# def set_username(sender, instance, **kwargs):
#             if not instance.username:
#                 instance.username = generate_username(instance)


# def save(self, *args, **kwargs):
#         if not self.username:
#             self.username = generate_username(self) #generate_username function from the controller
#         super(AdminUser, self).save(*args, **kwargs)



class Gallery(models.Model):
    user_id = models.ForeignKey(AdminUser,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/galleries', height_field=None, width_field=None, max_length=100)
    top_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

class faq(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    status = models.BooleanField(default=False, help_text="0=default, 1-Active")

    def __str__(self):
        return self.name

class blog(models.Model):
    img = models.ImageField(upload_to="img/blogImg/", blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    author_img = models.ImageField(upload_to="img/authorImg/", blank=False)
    slug = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.title