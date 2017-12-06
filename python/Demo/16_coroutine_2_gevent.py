#!/usr/bin/env python
# -*- coding: utf-8 -*-

# brew install libevent
# sudo easy_install greenlet
# install gevent in pycharm

# greenlet 基本思想:
# 当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，
# 等到IO操作完成，再在适当的时候切换回来继续执行

from gevent import monkey; monkey.patch_signal()
import gevent, time

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
    time.sleep(1)

g1 = gevent.spawn(f,5)
g2 = gevent.spawn(f,5)
g3 = gevent.spawn(f,5)

g1.join()
g2.join()
g3.join()

# 运行以上代码, 可以看到，3个greenlet是依次运行而不是交替运行。

# 要让greenlet交替运行，可以通过gevent.sleep()交出控制权：
print '\n使用gevent.sleep()让greenlet交替运行:'
def fun(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)

f1 = gevent.spawn(fun,5)
f2 = gevent.spawn(fun,5)
f3 = gevent.spawn(fun,5)

f1.join()
f2.join()
f3.join()

# 可以看到, 3个greenlet交替运行

# 在实际代码里, 不会使用gevent.sleep() 去切换协程,
# 而是在执行到io操作时, gevent自动切换, 代码如下:
