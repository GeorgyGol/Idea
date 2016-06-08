#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse
from . import test
from django.http.response import HttpResponseRedirect

# Create your views here.

strShowConst='show'
strHideConst='hide'

def first(request):
    
    #request.session.clear()
    
    request.session['vis_idea']='hide'
    request.session['vis_proj']='hide'
    request.session['vis_task']='hide'
    return render_main(request)
    
def render_main(request):
    vis={ k: v for (k, v) in request.session.items() if k.startswith('vis_')  }
    swt={ k.replace('vis_', 'sw_'): (lambda x: '<' if x==strHideConst else '>')(v) for (k, v) in vis.items() }
    vis.update(swt)
    return render_to_response("main.html", vis)

def index(request, sbt_what='idea', swt_comm=strHideConst):
    
    #res='''
    #<h1>Glavnuj vrode site!!</h1>
    
    #'''
    #return HttpResponse(res + "<BR/>")
    #users_list = test.readUserDB_list()
    #context=RequestContext(request, {  })
    #return render_to_response(r'main.html', context)
    #return HttpResponse(r'/main.html') 
    print(sbt_what, swt_comm)
    request.session['vis_' + sbt_what] = strShowConst if swt_comm == strHideConst else strHideConst
    return render_main(request)