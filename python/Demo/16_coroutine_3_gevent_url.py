#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在实际代码里, 不会使用gevent.sleep() 去切换协程,
# 而是在执行到io操作时, gevent自动切换, 代码如下:

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def f(url):
    print 'GET: %s' %url
    resp = urllib2.urlopen(url)
    data = resp.read()
    print '%d Bytes read from %s.' %(len(data), url)

gevent.joinall([
    gevent.spawn(f,'http://www.sina.com.cn/'),
    gevent.spawn(f,'http://www.aliexpress.com/'),
    gevent.spawn(f,'http://www.zcy.gov.cn/')
])

# 从结果看，3个网络操作是并发执行的，而且结束顺序不同，但只有一个线程。