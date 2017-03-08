from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view), 
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/invalid/$', views.invalid_login),
    url(r'^accounts/register/$',views.register),
    url(r'^client/main/$', views.client_main),
    url(r'^client/project/register/$', views.project_register),
    url(r'^parter/main/$', views.partner_main),
    
               
]