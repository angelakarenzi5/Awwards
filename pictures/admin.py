from django.contrib import admin
from .models import Profile

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('likes',)

admin.site.register(Profile)