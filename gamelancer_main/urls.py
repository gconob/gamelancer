from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views
from django.conf import settings
from django.conf.urls.static import static
  
urlpatterns = [    
    url(r'^$', views.index, name='index'),
    url(r'^terms-of-service/$', views.terms_of_service, name='terms_of_service'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view), 
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/accounts/login'}),
    url(r'^accounts/register/$',views.register),
    url(r'^client/main/$', views.client_main),
    url(r'^client/project/register/$', views.project_register),
    url(r'^client/project/main/$', views.project_main),
    url(r'^client/project/(?P<project_id>[0-9]+)$', views.project_detail, name='client_project_detail'),
    url(r'^client/apply/main/$', views.client_apply_manage, name='client_apply'),
    url(r'^client/user/info/$', views.client_user, name='client_user'),
    url(r'^client/user/password/$', views.client_password_change, name='client_password_change'),
    url(r'^client/user/account/$', views.client_account, name='client_account'),
    url(r'^client/user/verify/$', views.client_verify, name='client_verify'),
    url(r'^partner/main/$', views.partner_main),
    url(r'^partner/manage/$', views.partner_manage),
    url(r'^partner/userinfo/$', views.partner_user_page),
    url(r'^partner/userinfo/resume/$', views.partner_resume, name='partner_school'),
    url(r'^partner/portfolio/$', views.partner_portfolio),
    url(r'^partner/portfolio/(?P<id>[0-9]+)/$', views.partner_portfolio_detail, name='partner_portfolio_detail'),
    url(r'^partner/portfolio/upload/$', views.partner_portfolio_upload),
    url(r'^partner/project/apply/(?P<id>[0-9]+)/$', views.partner_project_apply),
    url(r'^partner/desc/$', views.partner_desc),
    url(r'^howto/main/$', views.howtouse_main),
    url(r'^howto/client/$', views.howotuse_client),
    url(r'^howto/partner/$', views.howtouse_partner),
    url(r'^howto/faq/$', views.howtouse_faq),
    url(r'^howto/fare/$', views.howtouse_fare),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
