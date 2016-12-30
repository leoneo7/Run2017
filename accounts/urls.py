from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^register/$', views.user_create, name= 'user_add'),
]


