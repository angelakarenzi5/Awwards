from django import forms
from .models import Profile

class CommentsForm(forms.Form):
    comment = forms.CharField(label='Comment',max_length=100)

# class NewProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         exclude = ['profile', 'pub_date','likes']
     

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'pub_date','likes']