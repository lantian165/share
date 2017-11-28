#/usr/bin/env python
# -*- coding: utf-8 -*-

'''
数据库是一个二维表, 表数据包含多行多列, 把一个表的内容用户python的数据结构表示出来的话,
可以用一个list表示多行, list的每一个元素是tuple, 表示一行记录, 比如:
[
  ('1', 'Michael'),
  ('2', 'Bob'),
  ('3', 'Amanda')
]

Python的DB-API返回的数据结构就是像上面这样表示的

但是tuple很看看出表的结构, 结果把一个tuple用class实例来表示, 可以更容易看出表结构

class User(Object):
    def __init__(self,id,name):
        self.id = id
        self.name = name

[
    ('1', 'Michael'),
    ('2', 'Bob'),
    ('3', 'Amanda')
]
这就是传说中的ORM技术: Object-Relational Mapping ,把关系数据库的表结构映射到对象上
'''

from sqlalchemy import Column, String, Integer, TIMESTAMP, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表名字:
    __tablename__ = 't_test'

    # 表的结构
    id = Column(Integer, primary_key=True)
    userId = Column(String(36))
    lastlogintime = Column(TIMESTAMP)

# 初始化数据库连接:
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 向数据库中插入一条记录, 可视为添加一个User对象

# 创建session对象
session = DBSession()

# 创建新User对象:
new_user = User(userId='Jane')

# 添加到session:
session.add(new_user)

# 提交即保存到数据库
session.commit()

# 关闭session():
session.close()

# 进行查询:
# 创建Session:
session2 = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user2 = session2.query(User).filter(User.id=='2').one()
# 打印类型和对象的name属性:
print '\ntype:', type(user2)
print 'name: [%s]' % user2.userId
print 'lastlogintime: [%s]\n' % (user2.lastlogintime)

# 关闭Session:
session2.close()



























