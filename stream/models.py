from django.db import models
from django import utils
# from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class anime(models.Model):
    # name=models.CharField(max_length=30)
    clue_id=models.IntegerField(primary_key=True)
    clue=models.CharField(max_length=30)
    def  __str__(self):
        return self

class user(AbstractUser):
    name=models.CharField(max_length=30)
    #last_name=models.CharField(max_length=30)
    #dob=models.DateField(default=utils.timezone.now)
    #email=models.EmailField()
    index=models.IntegerField(default=0)
    c01= models.IntegerField(default=0)
    c02= models.IntegerField(default=0)
    c03= models.IntegerField(default=0)
    c04= models.IntegerField(default=0)
    c05= models.IntegerField(default=0)
    c06= models.IntegerField(default=0)
    c07= models.IntegerField(default=0)
    c08= models.IntegerField(default=0)
    c09= models.IntegerField(default=0)
    c10= models.IntegerField(default=0)
    c11= models.IntegerField(default=0)


# class Profile(models.Model):
#     user = models.OneToOneField(user, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self):
#         super().save()

#         img = Image.open(self.image.path) # Open image
        
#         # resize image
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size) # Resize image
#             img.save(self.image.path) # Save it again and override the larger image



#--------session handling---------
# Model to store the list of logged in users
class LoggedInUser(models.Model):
    user = models.OneToOneField(user, related_name='logged_in_user',on_delete=models.CASCADE)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username