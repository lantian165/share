#/usr/bin/evn python
# -*- coding: utf-8 -*-

# 一个web应用的本质就是:
'''
1. 浏览器发送一个HTTP请求；

2. 服务器收到请求，生成一个HTML文档；

3. 服务器把HTML文档作为HTTP响应的Body发送给浏览器；

4. 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活, 这些可以调用统一的接口来实现,
开发者不需要重复造轮子, 只需要将精力专注于web业务.

这个接口就是 WSGI: Web Server Gateway Interface.
'''

# 定义一个函数供 server来调用, 名字不一定要为: application, 也可以为其它
def application(environ,start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return '<h1>Hello, web!</h1>'
    # return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return '<h1>environ[User-Agent]= %s!</h1>' % (environ['User-Agent'][1:] or 'web')

# application参数含义:
# 1. environ: 一个包含所有HTTP请求信息的 dict 对象
# 2. start_response: 一个发送http响应的函数

# start_response()函数接收两具参数:
# 1. http响应码
# 2. 一组list表示的http header, 每个header用一个包含两个str的tuple表示.

# application函数的返回值将作为http响应的Body发送给浏览器
