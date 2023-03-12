# from main.models import AdminUser
# # form auto generating username 
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.utils.text import slugify


# def generate_username(instance):
#     username = slugify(instance.name)
#     counter = 1
#     while instance.__class__.objects.filter(username=username).exists():
#         username = f'{username}-{counter}'
#         counter += 1
#     return username


# @receiver(pre_save, sender=AdminUser)
# def set_username(sender, instance, **kwargs):
#     if not instance.username:
#         instance.username = generate_username(instance)



# def save(self, *args, **kwargs):
#     if not self.username:
#         self.username = generate_username(self) #generate_username function from the controller
#     super(AdminUser, self).save(*args, **kwargs)


    