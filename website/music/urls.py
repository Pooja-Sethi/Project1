from django.conf.urls import url
from . import views

app_name = 'music'
urlpatterns = [
    # /music/ -->home page with no extra information
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/71/-->71 is the unique id or the primary key of the albums
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #music/album/2/                                              #2 is the pk of album you want to update
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/71/favorite/-->when a request directs to another web page or some logic  & not the same web page
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),---> delete this if use generic view and change view function  into class

]