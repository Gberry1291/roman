from django.urls import path,re_path

from . import views
from django.contrib import admin
from django.conf.urls import include


app_name='roman'


urlpatterns= [
    path('',views.Homepage.as_view(),name='home'),
    path('contact',views.Contactpage.as_view(),name='contact'),
    path('about',views.Aboutpage.as_view(),name='about'),
    path('calander',views.Calander.as_view(),name='calander'),
    path('saveday',views.SaveDay.as_view(),name='saveday'),
    path('mailinglist',views.MailingList.as_view(),name='mailinglist'),
    ]
