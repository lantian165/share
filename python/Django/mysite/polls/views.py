# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render

from django.http import HttpResponse
#from django.template import loader

from .models import Question

# Create your views here.

# Version 1:
'''
def index(request):
    return HttpResponse("Hello, baochen. Your's at the polls index.")
'''

# Version 2:
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
'''

# Version 3:
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''

# Version 4: shortcut render()
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request,'polls/index.html', context)

# Version 1:
'''
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
'''

# Version 2:
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request,'polls/detail.html',{'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# This is the simplest view possible in Django.
# To call the view, we need to map it to a URL
# - and for this we need a URLconf

# Reading to:
# url: https://docs.djangoproject.com/en/1.11/intro/tutorial03/
# A shortcut: get_object_or_404()
