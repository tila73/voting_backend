from main.models import User
# form auto generating username 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


def generate_username(instance):
    username = slugify(instance.name)
    counter = 1
    while instance.__class__.objects.filter(username=username).exists():
        username = f'{username}-{counter}'
        counter += 1
    return username


@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = generate_username(instance)