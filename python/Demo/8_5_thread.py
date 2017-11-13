#/usr/bin/evn python
# -*- coding: utf-8 -*-

# Python的线程是真正的Posix Thread, 而不是模拟出来的线程
# 模块thread是低级模块, threading对该模块进行了封装, 是高级模块

#启动一个线程就是把一个函数传入并创建Thread实例, 然后调用 start()开始执行

print '\n\n--------------------------------- Part 1: 线程的创建 ---------------------------------------'

import time, threading

def loop():
    print 'thrad %s is running ...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)

    print 'Thread %s ended.' % threading.current_thread().name

print '\nThread %s is running...' % threading.current_thread().name

# 调用方法: loop 创建子线程, 并指定线程的名字为: LoopThread
t = threading.Thread(target=loop, name='LoopThread')

# 开始执行这个线程
t.start()

# 等待线程结束
t.join()

# current_thread()方法永远返回当前线程的实例
# 主线程的实例叫 MainThread, 子线程的实例在创建时指定
print '\nThread %s ended.' % threading.current_thread().name

print '\n\n--------------------------------- Part 2: 锁机制 ---------------------------------------'

'''
由于线程的调度是操作系统执行的, 一个共享变量 blance, 初始值为0, 经过多个线程多次的引用, 赋值,
其值就有可能不按预期的方式发生变化
'''

# 高级语言的一条语句在CPU执行时是苦干条语句, 即使是一个简单的计算
# blance = blance + 5, 也分两步执行:
# 1. x = blance + 5
# 2. blance = x

print '\n下面的例子示范多线程共同访问一个变量是如何把变量的值弄成不可预期的:'

# 假定这个银行存款
blance = 0

def change_it(n):
    #先存后取, 正常每次输出的 blance 都应该是0
    global blance
    blance = blance + n
    blance = blance -n
    #print 'blance=%d' % blance

def run_thread(n):
    for i in range(50000):
        change_it(i)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print '\nAfter t1.join, t2.join, Blance=%d' % blance


'''
上述语句CPU可能的调度顺序为:

(正常的, 预期中的调度逻辑)
t1: t1.x=0+5      t1.x=5
t1: blance=t1.x   blance=5
t1: t1.x=blance-5 t1.x=0
t1: blance=t1.x   blance=0

t2: t2.x=0+8      t2.x=8
t2: blance=t2.x   blance=8
t2: t2.x=blance-8 t2.x=0
t2: blance=t2.x   blance=0

(CPU不按套路出牌, 随意中断并执行另外一个线程)
( t1, t2两个进程随机交替执行, blance的值就一定是0 )
t1: t1.x=0+5      t1.x=5
t1: blance=t1.x   blance=5

# 在这里, CPU 中断对t1进程的执行 转而调度执行 t2
t2: t2.x=0+8      t2.x=8
t2: blance=t2.x   blance=8

# 在这里, CPU 中断对t2进程的执行 转而调度执行 t1
t1: t1.x=blance-5 t1.x=3
t1: blance=t1.x   blance=3

t2: t2.x=blance-8 t2.x=-5
t2: blance=t2.x   blance=-5

'''

# 如果要确保 blance的计算正确, 就要给 change_it()加上一把锁,
# 确认当某个线程在执行 change_it()时, 其它线程不能同时更改change_it()里的变量
# 保证 change_it()对变更的赋值及更改是可预期的

# 创建一个锁可以通过 threading.Lock()来实现
blance = 0
lock = threading.Lock()

def run_thread_safe(n):
    for i in range(50000):
        # 先要获得锁:
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完了一个要释放锁:
            lock.release()

t3 = threading.Thread(target=run_thread_safe, args=(5,))
t4 = threading.Thread(target=run_thread_safe, args=(8,))

t3.start()
t4.start()

t3.join()
t4.join()

print '\n增加了锁之后\nAfter t3.join, t4.join, Blance=%d' % blance

# 获得了锁一定要记得释放, 否则那些苦等锁的线程将永远等待下去, 成为死线程
# 我们用try ... finally 来确保锁一定会释放

# 使用锁的好处是确保了一段关键代码只能由一个线程从头到尾完整地执行
# 坏处也很明显, 就是阻止了多线程的并发执行
# 包含锁的某段代码只能以单线程的方式执行, 大大降低了效率.
# 如果同时存在多个锁, 线程之间互相等待对方释放锁时, 就有可能造成死锁, 导致所
# 有线程都挂起. 既不能执行, 也无法终止, 只能由操作系统强行终止.

import threading, multiprocessing
def loop_test():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop_test)
    t.start()
    t.join()

# 使用C , C++, JAVA来写相同的代码, 可以把全部的核心跑满, 但是python就是不行
# 原因:
'''
Python 解释器在执行代码时, 有一个GIL锁: Global Interpreter Lock,
任何Python线程执行前, 必须先获得GIL锁, 每执行100条字节码, 解释器就自动释放GIL锁,
让其它线程有机会执行. 本质上这种设计给所有的线程都加上了锁, 造成多线程在python中只能交替执行.
即使有100个线程跑在100核的CPU上, 也只能用到1个核.

如果一定要让多线程用到多核, 只能通过C扩展来实现.
也可以通过多进程实现多核任务. 多个Python进程各自有独立的GIL锁, 互不影响.
'''