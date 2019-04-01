from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='gram/', blank=True)
    bio= models.CharField(max_length =1000)
    contact=models.CharField(max_length =100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

def __str__(self):
        return self.user_name
        
def save_profile(self):
        self.save()

class Meta:
        ordering = ['user_name']

def __str__(self):
        return self.name
