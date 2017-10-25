#/usr/bin/env python
# -*- coding: utf-8 -*-

# 高级特性的使用

print "\n--------- 1.切片 -----------"
# 以打印列表list为例
r = []
for i in range(1,31):
    r.append(i)

# 一般情况下只能用循环来打印list的值
print '使用普通方法打印List:'
for i in range(0,10,1):
    print r[i]

print '\n打印倒数第一个元素:'
print r[-1]

# 用切片特性来打印 List 前10个元素
print '\n用 切片 特性打印List:'
print '打印前10个元素:'
print r[0:10]

print '\n打印前5个元素:'
print r[:5]

print '\n切片打印 第10 to 20个元素:'
print r[10:20]

print '\n打印最后10个元素:'
print r[-10:]

print '\n取前10个数, 每两个取一个:'
print r[:10:2]

print '\n所有数,每5个取1个:'
print r[::5]

print '\n只用一个:打印整个列表:'
print r[:]

print '\n字符串也可以看成是一种List, 同样可以用切片来截取字符串:'
str='1234567890'
print str[:8]
# 用切片不用担心数组下标越界
print str[:20:2]

print "\n--------- 2.迭代 -----------"
# python 中使用for循环时, 只要对象是可迭代的, for循环就能正常运行
# 不需要担心该对象是List或者其它数据类型

# 如何判断一个对象是否为可迭代
# 可通过 collections模块的iterable类型来判断
from collections import Iterable

if isinstance('abc', Iterable):
    print '\'abc\' 是一个可迭代的对象'
else:
    print '\'abc\' 不是一个可迭代的对象'

'''  这段只能在命令行下验证, 在程序文件中解析代码会报错
if isinstance(abc, Iterable):
    print 'abc 是一个可迭代的对象'
else:
    print 'abc 不是一个可迭代的对象'
'''

d = { 'a': 1, 'b': 2, 'c': 3}
print '\n通过迭代的方式打印 key-value 字典数据:'
for i in d:
    print i

# list.itervalues() 用于直接把values返回成列表
print '\n打印dict迭代的 value:'
for i in d.itervalues():
    print i

# 同时迭代输出 key 和 value
print '\n同时迭代输出 key 和 value:'
for k,v in d.iteritems():
    print '(%s=%s) ' %(k,v)

print '\n复习: 打印 key a 对应的 value'
print d['a']

# for 循环同时打印两个变量的值
print '\nfor 循环同时打印两个变量的值:'
for x, y  in [('L1','R1'),('L2','R2'),('L3','R3')]:
    print '(x,y)=(%s,%s)' %(x,y)

print "\n--------- 3.列表生成式 -----------"
#要生成 [1,2,3,4,5,6,7,8,9,10] 可以使用 range(1,11)
# 但如果要生成 [1*1, 2*2, 3*3, ... , 9*9, 10*10], 则可如下方法来操作:
l = [x*x for x in range(1,11)]

print '\n使用列表生成式[x*x for x in range(1,11)]得到的结果为:'
print l[:]

print '\n还可以在列表生成式后加条件判断,例如只输出偶数的平方数:'
print [x*x for x in range(1,11) if x%2==0]

print '\n使用两层循环,可以生成全排列'
# 列表里的汉字print会输出编码, 不是汉字
#print [ t + d for t in '甲乙丙丁戌' for d in '子丑寅卯辰']
print [m + n for m in '12345' for n in 'abc']

print '\n用简洁的一行代码列出当前目录下的所有文件:'
import os
print [d for d in os.listdir('.') ]

print '\n也可以使用两个变量来将字典dict转换生成列表List:'
d = {'a':'1', 'b':'2', 'c':'3'}
print [ x + '=' + y for x, y in d.iteritems()]

print '\n从一个列表推导出另一个列表:'
l1 = ['APPLE','BANANA','PEACH']
print [ s.lower() for s in l1 ]

print "\n--------- 4.生成器 (generator) -----------"
print '\n通过列表生成式是一次性生成整个列表,如果元素特别多, 势必要占用很大的内存'
print '通过 生成器, 可以根据一定的规则在循环中不断地推算出后续的元素,不必一次性创建完整的list,从而节省大量空间'
print '要创建一个列表生成器有多种方法'
print '\n方法1: 直接把列表生成式的[]替换成()'
# 原来: [x*x for x in range(1,11)]
g =  (x*x for x in range(1,11))
# 可以用方法 g.next()打印出元素
print '生成器生成的第一个元素:' , g.next()
print '生成器生成的第二个元素:' , g.next()
# g.next() 到末尾的时候, 会抛出一个 StopIteration的错误. 一般不用这种方法取值
# 可使用如下方法更简洁
print '\n使用迭代的方式打印生成器内的元素:'
for i in g:
    print i

print '\n方法2: 利用yield 生成 generator函数:'
# 通过在函数内使用 yield 将函数变成:generator函数, 可以根据一定的规则生成列表
# 函数在运行时, 遇到 yield 就会返回.在下一次调用时next()时, 会从yield语句处开始执行
# 以斐波拉契数列为例:
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a,b = b, a + b
        n = n + 1

print '\n输出斐波拉契数列的前6个元素:'
fib(6)

def fib_yield(max):
    n,a,b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

print '\n生成generator函数后,fib(8)的执行结果:'
l = fib_yield(8)
for i in l:
    print i

print '\nyield函数原理验证函数'
def odd():
    print 'step 1'
    yield
    print 'step 2'
    yield
    print 'step 3'

o = odd()

# 每一个调用next(), 都执行到yield返回, 下次再从该语句处开始执行
for i in o:
    o.next()
