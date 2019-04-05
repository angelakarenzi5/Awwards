from rest_framework import serializers
from .models import Profile , Project

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'description', 'price')

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'price')