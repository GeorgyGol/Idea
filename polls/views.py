from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #templ = loader.get_template('polls/index.html')
    context=RequestContext(request, { 'latest_question_list': latest_question_list, })
    return render(request, 'polls/index.html', context) 

def detail(reques, question_id):
    return HttpResponse("You'er looking at question %s" % question_id)

def results(request, question_id):
    response="You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
