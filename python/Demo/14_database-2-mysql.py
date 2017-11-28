#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

# 连接时传入use_unicode=True, 让MYSQL的DB-API始终返回Unicode
conn = mysql.connector.connect(user='root',password='root',database='test',use_unicode=True)
cursor = conn.cursor()

cursor.execute('select * from t_test where id = 1')
values = cursor.fetchall()

print 'Query result: ', values

cursor.close()

conn.close
