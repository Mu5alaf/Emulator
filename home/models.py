from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class App(models.Model):
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE)
    apk_name = models.CharField(max_length=50)
    apk_path = models.FileField(upload_to='Apk/')
    first_screen_path = models.ImageField(upload_to='screenshots/',blank=True,null=True)
    second_screen_path = models.ImageField(upload_to='screenshots/',blank=True,null=True)
    video_record_path = models.FileField(upload_to='videos/',blank=True,null=True) 
    ui_hierarchy = models.TextField(null=True, blank=True)
    screen_changed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.apk_name