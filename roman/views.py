from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core import serializers
from django.conf import settings
from roman.models import Day
import json

class Homepage(TemplateView):
    template_name= 'roman/home.html'
    def get(self, request):


        args = {}
        return render(request,self.template_name,args)

class Calander(TemplateView):
    template_name = 'roman/calander.html'

    def get(self, request):

        daylist= Day.objects.all()
        daydic={}
        for day in daylist:
            endtime = str(day.date.day)+"-"+str(day.date.month)+"-"+str(day.date.year)
            daydic[endtime]={"date":endtime,"closed":day.closed}


        args = {"daylist":daydic}

        if request.session.get('newevent'):
            args["signininfo"]={"alert":"yes","text":"Reservation Set"}
            del request.session['newevent']

        if request.session.get('eventinuse'):
            args["signininfo"]={"alert":"yes","text":"Couldnt book your reservation,something went wrong. send an email directly to us!"}
            del request.session['eventinuse']

        return render(request,self.template_name,args)

class SaveDay(TemplateView):
    template_name = 'orange/calander.html'
    def post(self,request):

        decodedword=json.loads(request.body.decode('ascii'))
        dateoption=decodedword["date"]
        appname=decodedword["appname"]
        appemail=decodedword["appemail"]
        apptime=decodedword["apptime"]
        appmessage=decodedword["appmessage"]

        try:
            chosen_day=Day.objects.get(date=dateoption)
        except ObjectDoesNotExist:
            chosen_day=Day(date=dateoption,closed=True)
            chosen_day.save()

        daylist= Day.objects.all()
        daydic={}
        for day in daylist:
            endtime = str(day.date.day)+"-"+str(day.date.month)+"-"+str(day.date.year)
            daydic[endtime]={"date":endtime,"closed":day.closed}

        response=JsonResponse(daydic)

        return response
