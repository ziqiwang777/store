# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
 

def production_process(request):  # index页面需要一开始就加载的内容写在这里
    context = {}
    return render(request, 'production_process.html', context)
    