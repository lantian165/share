#/usr/bin/evn python
# -*- coding: utf-8 -*-

import os
# from 模块 import 类
from multiprocessing import process

print 'My pid is: ' , os.getpid()

print '\n运行 os.fork() 创建出子进程'
print 'fork()运行一次会返回两次'
pid = os.fork()

if pid == 0:
    print '\n在子进程:'
    print 'I am a child process, my pid is: ' , os.getpid()
    print 'my parent pid is:', os.getppid()
else:
    print '\n在父进程:'
    print 'I create a child process, its pid is: ' , pid

