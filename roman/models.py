from django.db import models

class Day(models.Model):

    def day_default():
        return {
        "1":"free",
        "2":"free",
        "3":"free",
        "4":"free",
        "5":"free",
        "6":"free",
        "7":"free",
        "8":"free",
        "9":"free",
        "10":"free",
        "11":"free",
        "12":"free",
        "13":"free",
        "14":"free",
        "15":"free",
        "16":"free",
        "17":"free",
        "18":"free",
        "19":"free",
        "20":"free",
        "21":"free",
        "22":"free",
        "23":"free",
        "24":"free"}

    date= models.DateTimeField()
    closed = models.BooleanField(default=False)
    times = models.JSONField(encoder=None, decoder=None,default=day_default)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['date']

class NewsLetter(models.Model):

    name= models.CharField(max_length=None)
    email= models.EmailField(max_length=254)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['email']

class HomeText(models.Model):

    numo= models.CharField(max_length=None)
    text= models.CharField(max_length=None)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['numo']

class AboutText(models.Model):

    numo= models.CharField(max_length=None)
    text= models.CharField(max_length=None)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['numo']
class HomePics(models.Model):
    name = models.CharField(max_length=255,unique=True)
    mainpic = models.ImageField(upload_to="roman/css/userpics",height_field=None,width_field=None,max_length=None,blank=True,null=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['name']
