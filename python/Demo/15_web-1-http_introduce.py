#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HTTP协议简介

'''
总结下HTTP请求的过程:
Step 1: 浏览器向服务器发送HTTP请求
方法:
  GET: 仅请求资源
  POST: 还会附带用户数据

路径:
  /full/url/path

域名:
   由HOST头指定
   HOST: www.sina.com.cn

其它相关的Header

如果是POST,那么请求还包括一个Body, 包含用户数据

Step 2: 服务器向浏览器返回HTTP响应
响应包括:
响应代码:
  200,  成功
  3xx,  重定向
  4xx,  客户端发送的请求有错误
  5xx,  服务器端处理时发生了错误

响应类型:
  由Content-Type指定

其它相关的Header

通常服务器的HTTP响应会携带一个Body, 网页的html源码就在Body中

Step 3: 如果浏览器还需要继续向服务器请求其它资源, 就再次发出http请求, 重复步骤1,2.

'''

'''
HTTP格式

每个HTTP请求和响应都遵循相同的格式, 一个HTTP包含Header和Body两部分, 其中Body是可选的.

HTTP GET 请求格式:
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

!!! 每个Header一行一个, 换行符是 \r\n.

HTTP POST 请求格式:
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...

!!! 当连续遇到两个 \r\n 时, Header部分结束, 后面的数据全部是Body.

HTTP响应的格式:
200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...

!!! HTTP响应如果包含Body, 也是通过 \r\n\r\n来分隔.
Body的数据类型由 Content-Type头来确定,
如果是网页, Body就是文本, 如果是图片, Body就是图片的二进制数据

当存在: Content-Endcoding时, Body数据是被压缩的, 最常见的压缩方式是gzip.
当看到 Content-Encoding: gzip时, 需要将Body数据先解压缩, 才能得到真正的数据.

'''















