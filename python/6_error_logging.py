#/usr/bin/env python
# -*- coding: utf-8 -*-

# 出现错误并不可怕,可怕的是不知道哪里出现错误

import logging

def foo(s):
    return 10/int(s)

def bar(s):
    print foo(s)*2

def main():
    try:
        bar('2')
    except StandardError, e:
        logging.exception(e)

main()

print '-------------------Part 1 END-------------------'

#import logging
logging.basicConfig(level=logging.INFO)

s = '1'
n = int(s)

logging.info('\nLOGINFO: n = %d\n' %n)
print '10/n = ', 10/n

print '-------------------Part 2 END-------------------'

