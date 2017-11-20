#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading, time

def tcplink(sock, addr):
    #print '[%s %s]: Accept a new connection from %s:%s...' % ( str(time.strftime('%Y-%m-%d %H:%M:%S')), addr )
    print 'Accept a new connection from %s:%s...' % ( addr )
    sock.send('Welcome!')

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send( 'Hello, %s!' % data )

    sock.close()

    print 'Connection from %s:%s closed.' % addr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口, 并绑定本机所有的网络地址
# bind(addr): the addr is a pair(host, port)
s.bind(('0.0.0.0', 8888))

# 监听端口, 并指定等待连接的最大数量
s.listen(5)

print 'Waiting for client to connection...'

while True:
    sock, addr = s.accept()

    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

    # 如果这行生效的话, 将会阻塞进而不能及时接收并发的连接请求
    # t.join()
