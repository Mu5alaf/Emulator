from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
"""
1 - using one to one field because ever user must have on user only
2 - using signals to auto create profile when user register
"""
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=25)
    image = models.ImageField(upload_to='profile/',null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    
    @receiver(post_save,sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)