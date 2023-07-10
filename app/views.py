from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    user=input('enter user topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=user)[0]
    TO.save()
    return HttpResponse('Topic is insertied ')

def insert_webpage(request):
    user=input('enter webpage user :')
    TO=Topic.objects.get_or_create(topic_name=user)[0]
    TO.save()
    n=input('enter webpage name :')
    u=input('enter user url :')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    
    return HttpResponse('Webpage is inserted')

def insert_accesrecord(request):
    user=input('enter webpage user :')
    TO=Topic.objects.get_or_create(topic_name=user)[0]
    TO.save()
    n=input('enter webpage name :')
    u=input('enter user url :')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('enter date :')
    writter=input('enter author name :')
    ACR=AccessRecord.objects.get_or_create(name=WO,date=d,author=writter)[0]
    ACR.save()
    return HttpResponse('AccessRecord data is submitted')