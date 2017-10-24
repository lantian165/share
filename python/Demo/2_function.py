#/usr/bin/env python
#-*- coding: utf-8 -*-


print "\n--------- Part 1 调用函数 -----------"
print abs(-100)


print "\n--------- Part 2 定义函数 -----------"

def get_abs(x):
    if(x>0):
        return x
    else:
        return -x

print 'get_abs(-5): ', get_abs(-5)
print 'get_abs(25): ', get_abs(25)

#空函数, 使用pass保证语法不报错
#空函数可用于点位,当函数暂不写时,先占个位子
print "\n--------- 空函数 -----------"
def to_be_improve():
    pass

print "\n--------- 函数参数数据类型检查 -----------"
# 重写get_abs()
def get_abs_new(x):
    if not isinstance(x,(int,float)):
        raise TypeError('parameter bad data type')
    if(x>0):
        return x
    else:
        return -x

# 调用函数时 A 要用引号引起来 否则会报错: 变更未定义
#print get_abs_new(A)

print "\n--------- 一次返回多个值 -----------"
# 在一个函数的return中一次性返回多个值, 比如说游戏中从一个点移动到另外一个点
# 给出坐标,位移,角度, 就需要返回一个二维坐标,三维坐标

# 导入数学函数包
import math
def move(x,y,step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x,y = move(100, 100, 60, math.pi/6)
print '游戏中移动坐标,一次返回两个值 x = %f, y = %f\n' %(x, y)

print 'python返回多个值其实是一种假象, 本质上是返回一个tuple\n'

print "\n--------- Part 3 函数的参数 -----------"

print "\n--------- 默认参数 -----------"

# 这个函数只能计划平方数
def power_1(x):
    if not isinstance(x,(int,float)):
        TypeError('Parameter Bad data type')
    return x*x

# 指定默认参数,在不指定参数时,默认计算平方数
def power_2(x, n=2):
    if not isinstance(x,(int,float)):
        TypeError('Parameter Bad data type')
    if not isinstance(n,(int,float)):
        TypeError('Parameter Bad data type')

    s = 1
    while n > 0:
        s = s * x
        n = n - 1

    return s

print '测试默认参数运行情况:'
print 'power(x,1) = ' , power_2(5,1)
print 'power(x)   = ' , power_2(5)
print 'power(x,3) = ' , power_2(5,3)

#使用默认参数的原则:
# 1. 必选参数在前,默认参数在后
# 2. 有从个默认参数时,变化大的默认参数放前面,变化小的默认参数放后面
# 使用默认参数可以降低函数调用时传参的难度

print '默认参数的坑:'
def add_end(L=[]):
    L.append('END')
    return L

print '\n正常调用add_end(\'1\',\'2\')时,输出为:'

#list_1 = ['1','2']
#add_end(list_1)
list_1 = add_end(['1','2'])
i = len(list_1)
# print '%s %s %s\n' %(list_1[0],list_1[1],list_1[2])
while i > 0:
    print '%d = %s' %(i,list_1[i - 1])
    i=i-1

print '\n使用默认参数调用add_end()时,输出为:'
list_1 = add_end()
i = len(list_1)
while i > 0:
    print '第一次默认调用 %d = %s' %(i,list_1[i - 1])
    i=i-1

list_1 = add_end()
i = len(list_1)
while i > 0:
    print '第二次默认调用 %d = %s' %(i,list_1[i - 1])
    i=i-1

list_1 = add_end()
i = len(list_1)
while i > 0:
    print '第三次默认调用 %d = %s' %(i,list_1[i - 1])
    i=i-1

print '可以看到3次独立的调用, 列表却是在前一次的基础上加长了\n'
print '原因解释如下:'
print '函数定义时,默认参数里的列表地址就被计算出来了,每次调用都要改变列表的内容'
print '也就造成每次调用输出都不一样'
print '\n因此\n要避免使用可变的内容作为默认参数'

print '为完善以上的函数, 可使用None\n'
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

print '\n完善后的函数使用默认参数调用add_end()时,输出为:'
list_1 = add_end()
i = len(list_1)
while i > 0:
    print '第一次默认调用 %d = %s' %(i,list_1[i - 1])
    i=i-1

list_1 = add_end()
i = len(list_1)
while i > 0:
    print '第二次默认调用 %d = %s' %(i,list_1[i - 1])
    i=i-1

list_1 = add_end()
i = len(list_1)
while i > 0:
    print '第三次默认调用 %d = %s' %(i,list_1[i - 1])
    i=i-1

print "\n--------- 传入数量可变的参数 -----------"
print '虽然可以用list or tuple来传入可变参数,但传参前需要先组装一个 list or tuple\n'
print '有更简洁的方法 函数定义时参数使用: *parameters'
def calc(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print 'sum =' , sum

print '定义了可变参数后函数的'
calc(1,2,3)

print "\n--------- Part 4 递归函数 -----------"




