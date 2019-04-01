from django.shortcuts import render , redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import  Profile
import datetime as dt
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def pictures_of_day(request):
    date = dt.date.today()
    pictures = Image.objects.all()
    return render(request, 'all-pictures/today-pictures.html', {'pictures':pictures})


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