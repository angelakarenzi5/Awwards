from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

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

class Project(models.Model):
    project_title = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'awards/', blank=True)
    project_details = models.CharField(max_length =100)
    profile=models.ForeignKey(Profile, null=True)
    link= models.CharField(max_length =100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    @classmethod
    def todays_pictures(cls):
                today = dt.date.today()
                pictures = cls.objects.filter(pub_date__date = today)
                return pictures

    @classmethod
    def days_pictures(cls,date):
                pictures = cls.objects.filter(pub_date__date = date)
                return pictures

    @classmethod
    def search_by_project(cls,search_term):
                project_title = Project.objects.filter(project_title__icontains=search_term)
                return project_title

class Votes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project =  models.ForeignKey(Project,on_delete=models.CASCADE)
    design = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
    usability = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
    content = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
      