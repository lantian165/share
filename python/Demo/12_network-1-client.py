#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect(addr): the addr is a pair(host, port)
s.connect(('127.0.0.1', 8888))

#print '[%s %s] Recv:[%s]' % ( time.strftime('%Y-%m-%d %H:%M:%S'), s.recv(1024))
print 'Recv:[%s]' % ( s.recv(1024))

for data in ['Mike', 'Anna', 'Sara']:
    s.send(data)
    print s.recv(1024)

s.send('exit')

s.close()
