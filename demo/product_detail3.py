# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
 

def product_detail3(request):  # index页面需要一开始就加载的内容写在这里
    context = {}
    
    return render(request, 'product_detail3.html', context)
    