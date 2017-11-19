# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, baochen. Your's at the polls index.")

# This is the simplest view possible in Django.
# To call the view, we need to map it to a URL
# - and for this we need a URLconf
