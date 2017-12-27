#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

# Part 1:
request = urllib2.Request("http://127.0.0.1:8000/polls/1/")
#request.add_header('content-TYPE', 'text/html; charset=utf-8')
response = urllib2.urlopen(request)

print response.getcode()
print response.geturl()
print response.read().decode("utf-8")

# Part 2:
'''
print '\nPart 2:\n'
request = urllib2.Request("http://127.0.0.1:8000/admin/polls/question/")
request.add_header('content-TYPE', 'text/html; charset=utf-8')
response = urllib2.urlopen(request)

print response.getcode()
print response.geturl()
print response.read()
'''
