from django.db import models

# Create your models here.
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