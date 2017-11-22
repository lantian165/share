#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sqlite的特点是轻量级， 可嵌入， 但不能承受高并发访问，
适合桌面和移动应用。

mysql是为服务器端设计的数据库，能承受高并发访问，
同时占用的内存也远远大于sqlite

mysql内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB
'''

#本例仅测试，未对可能抛出的异常做处理

#

# 导入sqlite驱动
import sqlite3

# 连接到sqlite数据库，数据文件是sqlite_test.db
# 如果文件不存在，会自动创建
conn = sqlite3.connect('sqlite_test.db')

# 建游标
sor = conn.cursor()

cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user (id, name) values(\'1\',\'Michael\')')

print 'cursor.rowcount=[%d]' % cursor.rowcount

cursor.execute('select * from user where id=?',('1',))

# 获取到结果集是列表形式存放的每一行
# 每行记录都是一个tuple数据
vaes = cursor.fetchall()

print 'values = ', values[:]

# 一定要记得关闭游标， 关闭连接， 否则会造成资源泄露
cursor.close()

# 一定要记得关闭游标， 关闭连接， 否则会造成资源泄露
conn.close()

# 如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。