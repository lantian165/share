# -*- conding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    # ex: /polls/5/
    # the var: question_id will be used in views.detail as parameter
    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),
]