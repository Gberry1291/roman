from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core import serializers
from django.conf import settings
from roman.models import Day, NewsLetter,HomeText,HomePics,AboutText
import json
from django.contrib.auth import get_user_model, authenticate, login
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class Homepage(TemplateView):
    template_name= 'roman/home.html'
    def get(self, request):

        bodytext={}
        words=HomeText.objects.all()
        for text in words:
            bodytext[text.numo]={"numo":text.numo,"text":text.text}

        homepics={}
        pics=HomePics.objects.all()
        for pic in pics:
            try:
                homepics[pic.name]=pic.mainpic.url
            except Exception as e:
                homepics[pic.name]="blank"


        args = {"bodytext":bodytext,"pics":homepics}

        return render(request,self.template_name,args)

class Contactpage(TemplateView):
    template_name= 'roman/contact.html'
    def get(self, request):


        args = {}
        return render(request,self.template_name,args)

class Aboutpage(TemplateView):
    template_name= 'roman/about.html'
    def get(self, request):

        bodytext={}
        words=AboutText.objects.all()
        for text in words:
            bodytext[text.numo]={"numo":text.numo,"text":text.text}

        homepics={}
        pics=HomePics.objects.all()
        for pic in pics:
            try:
                homepics[pic.name]=pic.mainpic.url
            except Exception as e:
                homepics[pic.name]="blank"


        args = {"bodytext":bodytext,"pics":homepics,"from":"adminhome"}
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

class MailingList(TemplateView):
    template_name = 'roman/home.html'
    def post(self,request):

        decodedword=json.loads(request.body.decode('ascii'))
        thename=decodedword["name"]
        theemail=decodedword["email"]

        message={"message":"Sie wurden in unsere Mailingliste aufgenommen, vielen Dank fürs Zuhören!"}

        try:
            newguy=NewsLetter.objects.get(email=theemail)
            message={"message":"Sie sind bereits für unseren Newsletter angemeldet!"}
        except ObjectDoesNotExist:
            newguy=NewsLetter(name=thename,email=theemail)
            newguy.save()

        response=JsonResponse(message)

        return response

class Editpage(TemplateView):
    template_name= 'roman/z_edit.html'
    def get(self, request):

        args = {}
        return render(request,self.template_name,args)

    def post(self,request):

        nameinput=request.POST.get('username')
        passinput=request.POST.get('password')

        user = authenticate(request, username=nameinput, password=passinput)
        if user is not None:
            login(request, user)

        return render(request,self.template_name)

class AdminHomepage(TemplateView):
    template_name= 'roman/z_home.html'
    def get(self, request):

        if not request.user.is_authenticated:
            return HttpResponseRedirect("edit")

        bodytext={}
        words=HomeText.objects.all()
        for text in words:
            bodytext[text.numo]={"numo":text.numo,"text":text.text}

        homepics={}
        pics=HomePics.objects.all()
        for pic in pics:
            try:
                homepics[pic.name]=pic.mainpic.url
            except Exception as e:
                homepics[pic.name]="blank"


        args = {"bodytext":bodytext,"pics":homepics,"from":"adminhome"}
        return render(request,self.template_name,args)

class AdminAboutpage(TemplateView):
    template_name= 'roman/z_about.html'
    def get(self, request):

        if not request.user.is_authenticated:
            return HttpResponseRedirect("edit")

        bodytext={}
        words=AboutText.objects.all()
        for text in words:
            bodytext[text.numo]={"numo":text.numo,"text":text.text}

        homepics={}
        pics=HomePics.objects.all()
        for pic in pics:
            try:
                homepics[pic.name]=pic.mainpic.url
            except Exception as e:
                homepics[pic.name]="blank"


        args = {"bodytext":bodytext,"pics":homepics,"from":"adminhome"}
        return render(request,self.template_name,args)

class SaveAdmin(TemplateView):
    template_name = 'roman/z_home.html'
    def post(self,request):

        body = request.body.decode("utf-8")
        data = json.loads(body)

        message={"message":"Saved"}

        if data["from"]=="home":
            for key, value in data.items():
                try:
                    newguy=HomeText.objects.get(numo=key)
                    newguy.text=value
                    newguy.save()
                except ObjectDoesNotExist:
                    newguy=HomeText(numo=key,text=value)
                    newguy.save()

        if data["from"]=="about":
            for key, value in data.items():
                try:
                    newguy=AboutText.objects.get(numo=key)
                    newguy.text=value
                    newguy.save()
                except ObjectDoesNotExist:
                    newguy=AboutText(numo=key,text=value)
                    newguy.save()

        response=JsonResponse(message)

        return response

class SavePic(TemplateView):
    template_name = 'roman/z_home.html'
    def post(self,request):

        next = request.POST.get('next', '/')
        nameo= request.POST.get('name')
        pic= request.FILES.get('pic')

        workingimage=HomePics.objects.get(name=nameo)
        workingimage.mainpic.delete()
        workingimage.mainpic=pic
        workingimage.save()


        return HttpResponseRedirect(next)

class EmailTemplate(TemplateView):
    template_name= 'roman/emailtemplate.html'
    def post(self, request):

        decodedword=json.loads(request.body.decode('ascii'))
        nameoption=decodedword["name"]
        emailoption=decodedword["email"]
        bod=decodedword["message"]


        text_content = render_to_string(
            "roman/email.txt",
            context={"message": bod,"fromtext":nameoption,"emailtext":emailoption,"footer":"--Hello From Garys email bot--"},
        )

        # Secondly, render the HTML content.
        html_content = render_to_string(
            "roman/emailtemplate.html",
            context={"message": bod,"fromtext":nameoption,"emailtext":emailoption,"footer":"--Hello From Garys email bot--"},
        )

        # Then, create a multipart email instance.
        msg = EmailMultiAlternatives(
            "New Question From Podcast Website!",
            text_content,
            "kuchtagary1@gmail.com",
            ["wideblitz@gmail.com"],
            headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
        )

        # Lastly, attach the HTML content to the email instance and send.
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        args = {"message":"Your message has been sent! We will contact you soon!"}
        response=JsonResponse(args)
        return response

class SendEmail(TemplateView):
    template_name= 'roman/sendemail.html'
    def get(self, request):

        userlist=NewsLetter.objects.all()
        args = {"userlist":userlist}

        return render(request,self.template_name,args)

    def post(self,request):

        body = request.body.decode("utf-8")
        data = json.loads(body)

        message={"message":"Saved"}

        subject=data["subject"]
        linktoimage=data["linktoimage"]
        emailmessage=data["message"]
        guys=data["guys"]

        text_content = render_to_string(
            "roman/newsletter.txt",
            context={"message":emailmessage,"linktoimage":linktoimage,"footer":"Thanks for listening"},
        )

        # Secondly, render the HTML content.
        html_content = render_to_string(
            "roman/newslettertemplate.html",
            context={"message":emailmessage,"linktoimage":linktoimage,"footer":"Thank you for Listening!"},
        )

        # Then, create a multipart email instance.
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            "kuchtagary1@gmail.com",
            guys,
            headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
        )

        # Lastly, attach the HTML content to the email instance and send.
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        response=JsonResponse(message)

        return response
