from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.pictures_of_day,name='picturesToday'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^view/profile/(\d+)', views.view_profile, name='view-profile'),
]
