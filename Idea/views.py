#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from . import test

# Create your views here.
def index(request):
    res='''
    <h1>Glavnuj vrode site!!</h1>
    
    '''
    return HttpResponse(res + "<BR/>")
    #users_list = test.readUserDB_list()
    #context=RequestContext(request, { 'user_list': users_list, })
    #return render(request, 'idea/main.html', context) 