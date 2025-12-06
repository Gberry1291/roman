from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core import serializers
from django.conf import settings

class Homepage(TemplateView):
    template_name= 'roman/home.html'
    def get(self, request):


        args = {}
        return render(request,self.template_name,args)
