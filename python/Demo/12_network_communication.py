#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 网络通信简单的理解就是两个进程之间在通信
# 这两个进程有可能在同一台机器上, 也有可能在不同机器上

# 导入socket库
import socket
#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET: 指定IPv4协议
# SOCK_STREAM: 指定面向流的TCP协议

# 建立连接 80 为web服务默认端口, 以便进行众所周知的访问
s.connect(('www.sina.com.cn', 80))

# 发送数据
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

#
data = ''.join(buffer)

# 关闭连接
s.close()

# 接收到的数据包含HTTP头和网页本身, 我们只需要把HTTP头和网页分离一下
# 把HTTP头打印出来, 网页内容保存到文件
header, html = data.split('\r\n\r\n', 1)
print "header=[%s]" % header

# 把接收到数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)





