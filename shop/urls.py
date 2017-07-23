from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^/upload/$', views.create, name='create'),    
    url(r'^/home/$', views.home, name='home'),    
    ]
