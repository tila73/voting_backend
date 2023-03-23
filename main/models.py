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
    event_title = models.CharField(max_length=150)
    event_description = models.TextField()
    event_date = models.DateField(("Date"), auto_now=False, auto_now_add=False)
    event_img = models.ImageField(upload_to='img/', blank=False, null=False)
    slug = models.CharField((""), max_length=100)

    def __str__(self):
       return self.event_title

 # model for News and News detail page   
class News(models.Model):
    news_title = models.CharField(("Title"), max_length=5100)
    news_description =models.TextField(("Description"))
    news_author = models.CharField(("Written By"), max_length=50)
    news_date = models.DateField(("News date"), auto_now=False, auto_now_add=False)
    news_img = models.ImageField(("Image"), upload_to='img/news/', height_field=None, width_field=None, max_length=None)
    slug = models.CharField(max_length=255)

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
    about_description = models.TextField()
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
    testimonial_img = models.ImageField(upload_to='img/testimonial', null=True)
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
    status = models.BooleanField(default=True , help_text="0=inactive, 1=active")

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

    def __str__(self):
        return self.title

class TeamMembers(models.Model):
    img = models.ImageField(upload_to='img/teams', blank=False, null=False)
    name = models.CharField(max_length=60)
    post = models.CharField(max_length=100)
    fb_link = models.CharField(max_length=150)
    twitter_link = models.CharField(max_length=150)
    insta_link = models.CharField(max_length=150)
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(("Name"), max_length=255)
    username = models.CharField(("Username"), max_length=255, unique=True)
    email = models.EmailField(("Email"), max_length=255, unique=True)
    password = models.CharField(("Password"), max_length=128)
    address = models.CharField(("Address"), max_length=100, null=True)
    phone_number = models.CharField(("Phone Number"), max_length=100)
    esewa_number = models.CharField(("Esewa Number"), max_length=100, null=True)
    role = models.IntegerField(("User Role"), default=1, help_text="0=business user(owner), 1=admin, 2=sub business user(owner)")
    status = models.BooleanField(default=True, help_text="0=inactive, 1=active" )
    created_at = models.DateTimeField(("Created date"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated Date"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/galleries', height_field=None, width_field=None, max_length=100)
    top_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

class faq(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    question = models.TextField(null=True)
    answer = models.TextField(null=True)

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
    
# model for event detail page
class EventDetails(models.Model):
    event_title = models.CharField(max_length=150)
    event_description = models.TextField()
    event_date = models.DateField(("Date"), auto_now=False, auto_now_add=False)
    event_img = models.ImageField(upload_to='img/', blank=False, null=False)
    slug = models.CharField((""), max_length=100)

    def __str__(self):
       return self.event_title

 # News detail page
class NewsDetails(models.Model):
    news_title = models.CharField(("Title"), max_length=5100)
    news_description = models.TextField(("Description"))
    news_author = models.CharField(("Written By"), max_length=50)
    news_date = models.DateField(
        ("News date"), auto_now=False, auto_now_add=False)
    news_img = models.ImageField(
        ("Image"), upload_to='img/news/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField()

    def __str__(self):
       return self.news_title


# About Details Model
class AboutDetails(models.Model):
    about_title = models.CharField(("Title"), max_length=100)
    about_description = models.TextField(("Description"), max_length=255)
    about_img = models.ImageField(
        ("Image"), upload_to='img/about/', height_field=None, width_field=None, max_length=None)
    status = models.BooleanField(
        default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.about_title

# blogDetails model
class blogDetails(models.Model):
    img = models.ImageField(upload_to="img/blogImg/", blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    author_img = models.ImageField(upload_to="img/authorImg/", blank=False)
    slug = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.title


# Testimonials DetailsModel
class TestimonialDetails(models.Model):
    testmoni_name = models.CharField(("Name"), max_length=50)
    testmoni_designation = models.CharField(("Designation"), max_length=30)
    testmoni_message = models.TextField(("Message"))
    status = models.BooleanField(
        default=True, help_text="0=inactive, 1=active")

    def __str__(self):
        return self.testmoni_name
    
class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    logo = models.ImageField(upload_to='img/business_logo', blank=False, null=True)
    img = models.ImageField(upload_to='img/business', blank=False, null=True)
    business_desc = models.TextField(null=True)

class Candidate(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    candidate_img = models.ImageField(upload_to='img/candidate', blank=False, null=True)
    candidate_name = models.CharField(max_length=55, null=True)
    total_vote = models.PositiveIntegerField(null=True)
    candidate_desc = models.TextField(null=True)
    
class candidate_payment(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    amount = models.CharField(max_length =5)
    transaction_id = models.CharField(max_length=10)
    esewa_status = models.BooleanField(default=True, help_text="0=inactive, 1=active")

class business_payment(models.Model):
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
    amount = models.CharField(max_length =5)
    transaction_id = models.CharField(max_length=10)
    esewa_status = models.BooleanField(default=True, help_text="0=inactive, 1=active")
    
