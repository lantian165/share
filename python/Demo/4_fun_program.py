#/usr/bin/env python
# -*- coding: utf-8 -*-

print "\n--------- 1.高阶函数 -----------"
print abs(-10)

print "\n--------- 1.1 变量指向函数的返回值 -----------"
# 把函数调用的结果赋给变量

x = abs(-20)

print '\n函数调用的结果保存在变量 打印该变量的值:'
print x

print "\n--------- 1.2 变量指向函数本身 -----------"
x=abs

print '变量指向函数后 x=abs, x(-30)=%d' %x(-30)

def max(a,b):
    if a > b:
        return a
    else:
        return b

print '验证自定义的max(a,b)函数, max( 100, 200 ) = %d' %max(100,200)

x = max
print '变量指向函数后 x=max, x(200, 300)=%d' %x(500, 300)

print '\n怎么理解函数名?\n函数名其实是一个指向函数的变量'
print 'python对于变量的类型并没有太严格的要求, 同一个变量既可以指定函数, 又可以指向常数'
max = 10.5
print 'max()原来是一个自定义的函数, 现在max = 10.5, 打印结果为: %.2f' %max
print '实际编程的时候, 永远不要这么做, 因为这会导致函数的定义丢失'

print "\n--------- 1.3 高除函数的定义 -----------"
print '既然变量可以指向函数, 函数的参数可以接收变量,那一个函数就可以作为参数传递给另一个函数'
print '\n像这样以函数作为参数的函数, 我们称为高阶函数'

f = abs

def add(x,y,fun):
    if not isinstance(x,(int,float)):
        TypeError('Date type must be int or float')
    if not isinstance(y,(int,float)):
        TypeError('Date type must be int or float')

    return fun(x) + fun(y)

print '将abs()作为参数传递给 add(10, -20, fun), 得到的结果为: %s' %add(10, -20, f)
# 恢复函数max原来的定义
max = x
print '恢复max函数的定义后, max(30, 20)=%d' %max(30,20)

print "\n--------- 1.4 map and reduce -----------"

print "\n--------- 1.4.1 map -----------"

print '如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。'
print '\n验证map(fun,list[])函数,把fun函数作用于第2个参数列表中的每一个元素:'
l = map(str,[1,2,3,4,5])
print '经过map(str,[1,2,3,4,5])后 得到的列表为:',l[:]
print '经过map(str,[1,2,3,4,5])后 得到的列表为:',l[0:3]
print '经过map(str,[1,2,3,4,5])后 得到的列表为:',l[0:-1]

def fxx(x):
    if not isinstance(x,int):
        TypeError('Datatype must be int')
    return x*x

rtn_list = map(fxx,[1,2,3,4,5,6])
print '\n验证返回平方数的map():'
print 'map(fxx,[1,2,3,4,5,6])返回的结果为: ', rtn_list[:]
print '另外一种打印列表的方式:', rtn_list

print "\n--------- 1.4.2 reduce -----------"
print 'reduce函数的作用, 就是递归的对列表里的元素执行fn函数'
def fn(x,y):
    return x*10 + y

print '\n验证fn函数, fn(1,3)=', fn(1,3)
print '\n验证reduce函数, reduce(1,3,5,7)=', reduce(fn, [1,3,5,7])

print "\n--------- 1.4.3 map 和 reduce 组合使用, str2int() -----------"

def str2int(s):
    def fn(x,y):
        return 10*x + y
    def char2num(x):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]
    return reduce(fn,map(char2num,s))

print '\n验证reduce(fn,map(char2num,s))\nstr2int(\'12345\')=' , str2int('12345')


print "\n--------- 1.5 filter() 列表筛选函数 -----------"
print '该函数用于过滤序列'

print '\nfilter()也接收一个函数和一个序列,依次用这个函数作用于序列中每一个元素'
print '根据返回值是true or false 决定是保留还是遗弃该元素,返回保留下来的元素列表'

def is_odd(n):
    return n%3 == 0

print '\n验证filter()函数:\nfilter(is_odd, [1,2,3,4,5,6,7,8,9,10]):' , filter(is_odd, [1,2,3,4,5,6,7,8,9,10])

print '\n把一个序列中的空字符去掉'
def not_empty(s):
    return s.strip()

print '去掉序列中的空字符串验证结果:' , filter( not_empty, ['A', '', 'B', '   ','C' ])

print "\n--------- 1.6 sorted() 列表排序函数 -----------"
print '\n验证排序函数执行结果:\nsorted([6,3,9,1,0,20,15])=' , sorted([6,3,9,1,0,20,15])

def reverse_str(s1,s2):
    u1 = s1.lower()
    u2 = s2.lower()

    if u1 > u2:
        return -1
    elif u1 < u2:
        return 1
    return 0

#print reverse_str('eabc','def')

print "\n验证排序函数执行结果:\nsorted(['abc', 'Book', 'Cool', 'Jump', 'Moon', 'Zoo']=" , \
     sorted(['abc', 'Book', 'Bool', 'Jump', 'Moon', 'Zoo'], reverse_str)

print "\n--------- 2 函数的返回值是函数 -----------"
print '\n我们通过这种方式来计算可变参数的求和:'
print '''def calc_sum(*args):
    s = 0
    for n in args:
        s = s + n
    return s'''
def calc_sum(*args):
    s = 0
    for n in args:
        s = s + n
    return s

print '验证: calc_sum(1,2,3,4,5) = ' , calc_sum(1,2,3,4,5)

print '\n如果不是要立即求和, 而是在后面需要使用时再计算该怎么办?'
print '这时可以返回求和的函数:'
print ''' 示例: 返回函数的函数:
def lazy_sum(*args):
    def sum():
        s = 0
        for n in args:
            s = s + n
        return s
    return sum
'''
def lazy_sum(*args):
    def sum():
        s = 0
        for n in args:
            s = s + n
        return s
    return sum

# 这时返回的参数和变量都保存在函数中, 我们称之为"闭包"
# 实际使用时应避免闭包内包含可被其它地方引用的局部变量
sum = lazy_sum(1,2,3,4,5,6)

print '\n验证结果: lazy_sum(1,2,3,4,5,6)=', sum()

'''
# 一段不被看好的挖坑测试代码
print '\n挖坑示例: 返回值是函数时, 不应该在函数中包含值有可能发生变化的情况'
def count():
    fs = []

    def f(i):
        return i*i

    for i in range(1,4):
        fs.append(f(i))

    return fs

f1 = count()

print '挖坑测试的结果: f1=, f2=', f1[:]
'''

print "\n--------- 3 匿名函数 -----------"
print '\n有的时候,不需要显示的定义函数, 只需要在调用于定义即可. 这样也可以避免函数名冲突'
print '举例验证:'
print '执行: map(lambda x:x*x,[1,2,3,4,5])=',  map( lambda x:x*x,[1,2,3,4,5] )

print "\n--------- 4 装饰器 decorator -----------"
def now():
    print '2013-02-29'

f = now
print "\n执行now():"
f()

print '\n定义装饰器函数, 让每次调用now()的时候, 额外打印一些日志:'
def log(func):
    def warpper(*args, **kw):
        print 'call fun %s():' % func.__name__
        return func(*args, **kw)
    return warpper

print '''\n装饰器函数的定义为:\ndef log(func):
    def warpper(*args, **kw):
        print 'call fun %s():' % func.__name__
        return func(*args, **kw)
    return warpper'''

print '\n调用方法: 借助python的@语法,把decorator置于函数的定义处:'
@log
def now():
    print '2013-03-29'

print '\n定义了decorator函数后 再调用now()函数的结果:'
now()

print "\n--------- 5 偏函数 -----------"
print'先举个偏函数应用的例子:'
print 'int(\'123456\')把字符串转为数值:' , int('123456')
print '其实调用时, int()的第二个参数默认为10, 也就是默认转换为10进制'

print '\n当要默认转换为二进制时,可使用偏函数更改函数的默认参数,并返回一个新的函数名'
import functools
int2 = functools.partial(int, base=2)
print 'int2(\'101\')把字符串转为二进制数值:%s'  %(int('101', base=2))

print '\n概念解释:'
print ''

