# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf


def company_introduction(request): 
    context = {}
    return render(request, 'company_introduction.html', context)


def company_introduction_eng(request):
    context = {}
    return render(request, 'eng_aboutus.html', context)
