from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TMF=TopicModelForm()
    d={'TMF':TMF}
    if request.method=='POST':
        TMFO=TopicModelForm(request.POST)
        if TMFO.is_valid:
            TMFO.save()
        return HttpResponse('data is submitted')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WMF=WebpageModelForm()
    d={'WMF':WMF}
    if request.method=='POST':
        WMFO=WebpageModelForm(request.POST)
        if WMFO.is_valid:
            WMFO.save()
        return HttpResponse('data is submitted')
    return render(request,'insert_webpage.html',d)

def insert_accessrecords(request):
    AMF=AccessRecordsModelForm()
    d={'AMF':AMF}
    if request.method=='POST':
        AMFO=AccessRecordsModelForm(request.POST)
        if AMFO.is_valid:
            AMFO.save()
        return HttpResponse('data is submitted')
    return render(request,'insert_accessrecords.html',d)