from django.db import models

# Create your models here.
class faq(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    status = models.BooleanField(default=False, help_text="0=default, 1-Active")

class blog(models.Model):
    img = models.ImageField(upload_to="img/blogImg/", blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    author_img = models.ImageField(upload_to="img/authorImg/", blank=False)
    slug = models.CharField(max_length=150, null=False, blank=False)