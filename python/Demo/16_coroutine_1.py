#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
# 所谓的切换是指在同一个线程中进行, 子程序的切换不是线程的切换, 而是程序自身控制. 没有线程切换的开销
#

# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

# Python通过yield提供了对协程的基本支持

import time

def consumer():
    r = ''
    while True:
        # consumer通过yield拿到消息，处理，又通过yield把结果传回
        m = yield r
        if not m:
            return
        print '[Consumer] Consuming %s...' %m

        time.sleep(1)

        r = '200 OK'

def produce(c):
    # 启动生成器
    c.next()
    n = 0

    while n < 5:
        n = n + 1
        print '[Produceer] Producing %s...' %n

        # 通过c.send(n)切换到consumer执行
        r = c.send(n)

        print '[Producer] Consumer return: %s\n' %r

    # produce决定不生产了，通过c.close()关闭consumer，整个过程结束
    c.close()

if __name__ == '__main__':
    c = consumer()

    produce(c)

# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务
