from django import forms
from .models import Project, Profile , Votes

class CommentsForm(forms.Form):
    comment = forms.CharField(label='Comment',max_length=100)

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile', 'pub_date','comment']
     

class VotesForm(forms.ModelForm):
    class Meta:
        model = Votes
        exclude = ['user', 'project','posted_on']