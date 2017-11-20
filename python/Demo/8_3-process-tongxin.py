#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' %value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(q)
        print 'Read %s from queue...' %value

if __name__ == '__main__':
    q = Queue()

    #创建写进程
    pw = Process(target=write, args=(q,))

    #创建读进程
    pr = Process(target=read, args = (q,))

    #启动写进程
    pw.start()

    #启动读进程
    pr.start()

    # 等待写进程结束
    pw.join()

    # 读进程是死循环， 需要强制结束
    pr.terminate()
