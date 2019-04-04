from django.shortcuts import render , redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import  Profile , Project , Votes
import datetime as dt
from .forms import ProfileForm , NewProjectForm , VotesForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def pictures_of_day(request):
    date = dt.date.today()
    pictures = Project.objects.all()
    return render(request, 'all-pictures/today_pictures.html', {'pictures':pictures})


# @login_required(login_url='/accounts/login/')
# def pictures_today(request):
#     if request.method == 'POST':
#         form = PicturesLetterForm(request.POST)
#         if form.is_valid():
#             print('valid')
#         form = PicturesLetterForm(request.POST)
#     else:
#         form = NewsLetterForm()

#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             email = form.cleaned_data['email']
#             recipient = PicturesRecipients(name = name,email =email)
#             recipient.save()
#             send_welcome_email(name,email)

#             HttpResponseRedirect('pictures_today')
#         else:
#             form = PicturesForm()
#     return render(request, 'all-pictures/today-pictures.html', {"pictures":pictures,"PicturesForm":form})


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
    return render(request, 'view_profile.html',{"profile":profile , "pictures":pictures},)


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
    else:
        form = VotesForm()
        return render(request, 'new_votes.html', {"form":form,'post':post,'user':current_user,'votes':votes})
