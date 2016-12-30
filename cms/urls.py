from django.conf.urls import url
from cms import views

urlpatterns = [
    url(r'^track/$', views.track_list, name='track_list'),
    url(r'^track/user/$', views.track_list_user, name='track_list_user'),
    url(r'^track/ranking/$', views.track_ranking, name='track_ranking'),
    url(r'^track/add/$', views.track_edit, name='track_add'),
    url(r'^track/mod/(?P<track_id>\d+)/$', views.track_edit, name='track_mod'),
    url(r'^track/del/(?P<track_id>\d+)/$', views.track_del, name='track_del'),
]