from django.urls import path,re_path

from . import views
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth import views as auth_views

app_name='roman'


urlpatterns= [
    path('',views.Homepage.as_view(),name='home'),
    path('admin/', admin.site.urls),
    path('contact',views.Contactpage.as_view(),name='contact'),
    path('about',views.Aboutpage.as_view(),name='about'),
    path('calander',views.Calander.as_view(),name='calander'),
    path('saveday',views.SaveDay.as_view(),name='saveday'),
    path('mailinglist',views.MailingList.as_view(),name='mailinglist'),
    path('sendemail',views.SendEmail.as_view(),name='sendemail'),
    path('question',views.EmailTemplate.as_view(),name='question'),
    path('edit',views.Editpage.as_view(),name='edit'),
    path('adminhome',views.AdminHomepage.as_view(),name='adminhome'),
    path('adminabout',views.AdminAboutpage.as_view(),name='adminabout'),
    path('saveadmin',views.SaveAdmin.as_view(),name='saveadmin'),
    path('savepic',views.SavePic.as_view(),name='savepic'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    ]
