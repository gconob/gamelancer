from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from gamelancer_main.models import Post
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="gamelancer_main/blog.html")),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view), 
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/invalid/$', views.invalid_login),
    url(r'^accounts/register/$',views.register),
    url(r'^client/main/$', views.client_main),
    url(r'^parter/main/$', views.partner_main)
    
               
]