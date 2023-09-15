from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from stream.models import LoggedInUser
from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver


# @receiver(post_save, sender=User) 
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()


#--------session handling---------

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user')) 


@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()