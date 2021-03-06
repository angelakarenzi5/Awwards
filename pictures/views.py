from django.shortcuts import render , redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import  Profile , Project , Votes
import datetime as dt
from .forms import ProfileForm , NewProjectForm , VotesForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
# Create your views here.




@login_required(login_url='/accounts/login/')
def pictures_of_day(request):
    date = dt.date.today()
    pictures = Project.objects.all()
    return render(request, 'all-pictures/today_pictures.html', {'pictures':pictures})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user=current_user
            project.save()
        return redirect('picturesToday')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user
            profile.bio=form.cleaned_data['bio']
            profile.photo = form.cleaned_data['profile_photo']
            profile.user=current_user
            
            profile.save()
        return redirect('picturesToday')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def view_profile(request, id):

    profile=Profile.objects.get(user_id=id)
    pictures = Project.objects.filter(user_id=id)

    return render(request, 'view_profile.html',{"profile":profile , "pictures":pictures})




def search_results(request):

    if 'project_title' in request.GET and request.GET["project_title"]:
        search_term = request.GET.get("project_title")
        searched_project_title = Project.search_by_project(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_project_title})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def view_project(request, id):

    project=Project.objects.get(id=id)
    votes = Votes.objects.filter(project = id).all() 

    design=0
    usability=0
    content=0
    num = len(votes)

    for n in votes:
        design+=round(n.design/num)
        usability+=round(n.usability/num)
        content+=round(n.content/num)
    return render(request, 'view_project.html',{"project":project ,"votes":votes,"usability":usability,"design":design,"content":content})

def votes(request,id):
    current_user = request.user
    post = Project.objects.get(id=id)
    votes = Votes.objects.filter(project=post)
  
    if request.method == 'POST':
            vote = VotesForm(request.POST)
            if vote.is_valid():
                design = vote.cleaned_data['design']
                usability = vote.cleaned_data['usability']
                content = vote.cleaned_data['content']
                rating = Votes(design=design,usability=usability,content=content,user=request.user,project=post)
                rating.save()   
                return redirect('picturesToday')
    else:
        form = VotesForm()
        return render(request, 'new_votes.html', {"form":form,'post':post,'user':current_user,'votes':votes})


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

