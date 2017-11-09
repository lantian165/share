#/usr/bin/evn python
# -*- coding: utf-8 -*-

print '\n------------------------------- Part 1 基本的文件IO操作 -----------------------------------------\n'

filename = '/Users/zcy/PycharmProjects/Demo/io_test'

try:
    f = open(filename, 'r')
    print f.read()
finally:
    if f:
        f.close()

print '如果每次都这么写太麻烦,可以用如下更简洁的方式, 读完了同样会关闭文件:\n'
print 'read()一次性输出整个文件的内容:'
with open( filename, 'r') as f:
    print f.read()


# 每一次调用read()都会一次性读取整个文件的所有内容, 如果文件有10G的话,就会一下把内存撑爆
# 为保险起见, 可以用read(size), readline()每次读取一部分内容
print '使用readline()每次读取一行,并通过strip()把换行符去除后打印出文件内容:'
with open(filename,'r') as f:
    str = f.readline()
    while str:
        str = str.strip()
        print str
        str = f.readline()
    #print f.read(9) # 一个汉字3个字节

print '\n读取二进制文件,比如: 图片, 视频等, 可以用"rb"模式读取'
print 'open(filename, \'rb\')'

print '\n如果要读取非ASCII编码的文件,就必须以二进制方式打开,再解码:'
print '''f=open(gdk_filename,\'rb\')
u = f.read().decode('gbk')
'''

print '写程序时每次都手动转码太麻烦, python帮我们提供了codecs模块来将文件自动转码为unicode:'
print '''import codecs
with codecs.open(gbk_filename, 'r', 'gbk') as f:
    f.read()
'''

print '写文件:'
#f = open(filename,'w')
with open(filename,'a')  as f:
    f.write('\n写入文件:\n这一行是测试写入文件用的\n')

print '\n打印出来写文件后的结果:'
with open(filename,'r') as f:
    print f.read()

print '写文件时,操作系统往往不会立即把内容写入磁盘,而是会先缓存起来,空闲时再慢慢写入.'
print '只有在调用了close()时, 才会保证把没写入的数据全部写入磁盘'
print '如果忘记调用close(), 就可能导致有部门数据没有写入到磁盘'

print '\n------------------------------- Part 2 操作目录和文件 -----------------------------------------\n'
print '操作系统的 dir, cp等命令只是简单的调用了操作系统提供的接口函数'
print 'python内置的os模板也可以直接调用操作系统提供的接口函数'

import os
print '\n通过os模板打印操作系统的名字:'
print os.name
print os.listdir('.')
print os.times()
print os.uname()

print '\n打印环境变量信息:'
print os.environ

print '\n打印PATH:'
print os.getenv('PATH')

print '\n操作文件和目录的函数一部分在os模块中, 另一部分在os.path模块中'
print '查看,创建和删除目录可以这么调用:'

print '\n查看当前目录的绝对目录:'
print os.path.abspath('.')

print '\n在当前目录下新建一个testdir目录:'
curdir = os.path.abspath('.')
newdir = os.path.join(curdir, 'testdir')
print '将要创建的新目录是:' , newdir

if os.path.exists(newdir):
    print '该目录已存在, 先将其删除'
    os.rmdir(newdir) # 也可以使用: os.remove(), 但都只能删除非空目录

if not os.path.exists(newdir):
    print '目录已删除成功'
else:
    print '目录删除失败'

print '现在创建的新目录:',  newdir
os.mkdir(newdir)
if os.path.exists(newdir):
    print '新目录已创建成功'

print '\n要拆分路径时,可使用如下方法: os.path.split(newdir)'
print '拆分后的结果为:'
print os.path.split(newdir)

print '\n复制文件的函数在os模块中并不存在, 原因是复制函数并非由操作系统提供的系统调用.但有shutil模块对os模块进行补充.'
print '\n列出当前目录下的所有目录:'
print [x for x in os.listdir('.') if os.path.isdir(x) ]

print '\n列出所有的文件:'
print [x for x in os.listdir('.') if os.path.isfile(x) ]
print '\n列出所有的.py文件:'
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']



print '\n------------------------------- Part 3 序列化 -----------------------------------------\n'
print '序列化的含义: 把运行时内存里的内容变成可以在磁盘上,网络上存储或传输的文件'
print 'python中, 序列化称为: pickling, 其逆向过程为反序列化, 称为: unpickling'
print 'python提供两个模块来实现序列化: cPickle和pickle,区别在于cPickle是C语言写的,速度较快, pickle是python写的, 速度较慢'
print '使用的时候, 先尝试导入cPickle, 不行再导入pickle'
print '''
try:
    import cPickle as pickle
except ImportError:
    import pickle
'''
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
print '对内存里的字典数据进行序列化:'
print pickle.dumps(d)

print '把序列化的内容存储在文件 dump.txt中'
with open('dump.txt','wb') as f:
    pickle.dump(d,f)

print '\n反序列化示例:'
with open('dump.txt','rb') as f:
    d1 = pickle.load(f)

print '\n反序列化读取到的内容为:'
print d1
print 'd1[age]=' , d1['age']

print 'JSON: 如果要在不同编程语言之间传递对象,就必须把对象序列化为标准格式, 比如XML, 但更好的方法是序列化为JSON.'
print 'json本向就是一个字符串, 可以被所有的语言读取, 并且可以方便的存储到磁盘并进行网络传输,并且可以在web页面直接读取'

print '\npython内置的json对象提供了非常完善的python到json格式的转换'

print '\n示例: 如果将一个python对象序列化为一个json对象:'
import json

d = dict(name='Bob', age=20, score=88)
print '使用json序列化后返回的结果为:'
# dumps()方法返回一个str,内容就是标准的json
print json.dumps(d)

print '\njson反序列化示例:'
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print '反序列经得到的结果为:'
# json反序列化默认得到所有的字符串都是unicode而不是str
print json.loads(json_str)
# 结果: {u'age': 20, u'score': 88, u'name': u'Bob'}
