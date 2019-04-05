from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.pictures_of_day,name='picturesToday'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^view/profile/(\d+)', views.view_profile, name='view-profile'),
    url(r'^/votes/(\d+)', views.votes, name='new-votes'),
    url(r'^view/project/(\d+)', views.view_project, name='view-project'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/profile/$', views.ProfileList.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
