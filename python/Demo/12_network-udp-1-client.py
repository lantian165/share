#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in ['Jack','Mike', 'Rose']:
    s.sendto(data, ('127.0.0.1',8888) )

    # 接收数据
    print s.recv(1024)

s.close()