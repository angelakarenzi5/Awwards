from rest_framework import serializers
from .models import Profile , Project

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'bio', 'contact' , 'user')

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_title', 'image', 'project_details','profile','link','user')