from django.urls import path,re_path

from . import views
from django.contrib import admin
from django.conf.urls import include


app_name='roman'


urlpatterns= [
    path('',views.Homepage.as_view(),name='home'),
    path('calander',views.Calander.as_view(),name='calander'),
    path('saveday',views.SaveDay.as_view(),name='saveday'),
    ]
