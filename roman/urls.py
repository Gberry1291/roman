from django.urls import path,re_path

from . import views
from django.contrib import admin
from django.conf.urls import include


app_name='roman'


urlpatterns= [
    path('',views.Homepage.as_view(),name='home'),
    ]
