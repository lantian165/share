#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, time, Queue
from multiprocessing.managers import BaseManager

# 创建发送任务的队列
task_queue = Queue.Queue()

# 创建接收任务的队列
result_queue = Queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda : task_queue)
QueueManager.register('get_result_queue', callable=lambda : result_queue)

# 绑定端口 5000, 设置验证码: abc
manager = QueueManager(address=('',5000), authkey ='abc')

# 启动 Queue
manager.start()

#获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print 'Put task %d...' %n
    task.put(n)

# 从result队列读取结果:
print '\nTry get results...'
for i in range(10):
    try:
        r = result.get(timeout=10)
        print 'Result: %s' %r
    except Queue.Empty:
        print 'task queue is Empty.'

# 关闭:
manager.shutdown()
print '\nClose manager.\n'







