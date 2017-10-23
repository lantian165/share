#/usr/bin/env python
#-*- coding: utf-8 -*-

a = 100

if a > 0:
    print "a>0"
else:
    print "a<0"

print '''\nline 1
line 2
line 3\n'''

boolvalue=False

if boolvalue:
    print "True"
else:
    print "False"

print '\n'
c="abc"
tmp=c
c="def"

print c
print tmp

print 10/3
print 10.0/3

print "print PI"
PI=3.1415926
R=6
print R**2
Circle=PI*R**2
print Circle

# charactor format:
# ASCII -> unicode -> utf-8 (一个utf-8一般占3个字节)
# 英文 -> 所有字符,定长存储 -> 所有字符, 变长存储
print "\n--------------------"
print "abc".decode('utf-8')
print "中文".decode('utf-8')
print len("abc")
print len("中文")

# unicode 字符串用 u'...'表示,如下打印 unicode
print
print u'中'

print "\n--------------------"

# 在python中,字符串格式化的方式与C语言中是一致的
print "Hi, %s, Your score is %d\n" %('Michael', 60)
print "The average score is %10.2f\n"  %( 700.0/6)
print "The percent of change is: %d%%\n" % ( 10 )

# list : 是一种有序集合, 可随时修改,添加或删除其中的元素
# 用classmate表示班级里的同学
print "\n--------------------"
classmates = ['宝琛', '冰霜', '晓明']
print len(classmates)
classmates.insert(1,'秋蓉')
classmates.append('永利')
print classmates[0],classmates[1],classmates[-2],classmates[-1]

# tuple也是一种有序元组,与list很相似,但一旦初始化就不能修改
classmates_gd = ('宝琛','燕东','艺平')
print classmates_gd[0],classmates_gd[1],classmates_gd[2]
# 打印一个越界的值, error_msg: tuple index out of range
# print classmates_gd[3]

# 不加逗号,当成数值赋值,加逗号,当成是初始化只有一个元素的tuple元组
t = (1)
m = (1,)

print t
print m[0]

# 来实验一个"可变的"tuple
print '\n来实验一个"可变的"tuple:'
n = ('x','y',['1','2'])
print n[0], n[1], n[2][0], n[2][1]
n[2][0]=3
n[2][1]=4
n[2].append(5)
print n[0], n[1], n[2][0], n[2][1],n[2][2]
# 实验的结论: 要保证tuple真正不可变, 其内部的元素也要都不可变

# 条件判断, 注意不要少写了冒号
print "\n--------- if else -----------"
age = 17
if age >= 18:
    print 'Your age is:', age
    print 'You\'re adult!'
else:
    print 'You\'re still a child'

# 循环
print "\n--------- for while -----------"
names = ['Jack','Mike','Rose']
for name in names:
    print name

sum = 0
for i in [1,2,3,4,5]:
    sum = sum + i
print 'sum =',sum

# 利用range()自动生成序列
print "\n--------- range() -----------"
for i in range(10,21,2):
    print i

print
for i in range(5):
    print i

sum = 0
for i in range(101):
    sum+=i
print '\nsum calc by 高斯 = %d' %(sum)

print "\n--------- while() -----------"
sum = 0
i=50

while i > 0:
    sum+=i
    i = i - 1
print 'sum from 1 to 50 = ', sum

# raw_input永远都以字符串作为返回值,如果需要返回整形,
# 就得用int()做强制转换

print "\n--------- raw_input() -----------"
'''
birthday = int(raw_input('Input the Birth Year:'))
print '出生年份是:',birthday
if birthday > 2000:
    print '00后'
else:
    print '00前'
'''

# dict 字典, key-value
print "\n--------- dict{} -----------"
d = {'宝琛':1987, '伟萍':1986, '苏里':2011}
print d['伟萍']

# 如果key不存在, 就会报错
# 要避免出现key不存在的情况,可以有两种办法:
# 1.利用 in 做判断
print '使用 in 来判断key是否在字典中:'
if '苏里' in d:
    print '苏里 in dict, it\'s birth =', d['苏里']
else:
    print '苏里 not in dict'
# 2.利用 get 方法:
print '使用 get 来判断key是否在字典中:'
if d.get('苏里-1') is None:
    print '苏里-1 not in dict'
else:
    print '苏里-1 in dict, it\'s birth =', d['苏里']

# list 与 dict 比较:
# list 特点: [] ()
#   占用内存小, 查找速度随数量增加而变慢
# dict 特点: {}
#   占用内存大, 查找速度不受数据量增加的影响

print "\n--------- set() -----------"
# set 和 dict类似, 不同的是set只有key, 而没有value
# 可以利用这个特性自动过滤重复元素
s = set([1,2,3,3,4,5])
print s
# add(key)添加元素
s.add(6)
print 'After add 6, the set is :', s
# remove(key)删除元素
s.remove(1)
print 'After remove 1, the set is :', s

# set 可以看作是数学上无序和无重复元素的集合,
# 两个 set 可做数学上的并集,交集
s1 = set([1,2,3])
s2 = set([3,4,5])
print 's1 & s2 = ', s1 & s2
print 's1 | s2 = ', s1 | s2
