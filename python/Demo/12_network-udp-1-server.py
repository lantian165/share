#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

# 使用UDP时, 不需要建立连接, 只要知道对方的IP端口和地址, 就可以直接发送数据包
# 但数据能不能到达就不知道了, 但优点是速度快

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 8888))

print 'Bind UDP on 8888...'

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)

    print 'Received from %s:%s...' % addr
    s.sendto('Hello, %s' % data, addr )