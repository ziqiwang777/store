# -*- coding: utf-8 -*-
#from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponseRedirect

from demo.models import Message
def contact_US(request):  # index页面需要一开始就加载的内容写在这里

    message = Message()

    if request.method == "POST":
        name = request.POST.get("name","")
        phone = request.POST.get("phone","")
        personal_info = request.POST.get("personal_info","")
        message_c = request.POST.get("message","")
        publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message.name = name
        message.phone = phone
        message.personal_info = personal_info
        message.message_c = message_c
        message.publish = publish
        message.save()
        return HttpResponseRedirect("/submitsuccess")


    if request.method == "GET":


        return render(request,"contact_US.html")

def submitsuccess(request):
    return render(request,"Response_Success.html")


def contact_US_eng(request):  # index页面需要一开始就加载的内容写在这里
    print("/here")

    message = Message()

    if request.method == "POST":
        name = request.POST.get("name","")
        phone = request.POST.get("phone","")
        personal_info = request.POST.get("personal_info","")
        message_c = request.POST.get("message","")
        publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message.name = name
        message.phone = phone
        message.personal_info = personal_info
        message.message_c = message_c
        message.publish = publish
        message.save()
        print("/eng_ss")
        return HttpResponseRedirect("/eng_ss")


    if request.method == "GET":


        return render(request,"eng_cs.html")

def submitsuccess_eng(request):
    print("/eng_ss")

    return render(request,"eng_submitsuccess.html")
