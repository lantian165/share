#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 数据库引擎对象:
class _Engine(object):
    def __init__(self, connect):
        self._connect = connect
    def connect(self):
        return self._connect()

engine = None

# 持有数据库连接的上下文对象:
class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transactions = 0

    def is_init(self):
        return not self.connection is None

    def init(self):
        self.connection = _LasyConnection()
        self.transactions = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection.cursor()

_db_ctx = _DbCtx()

# 由于_db_ctx是threadlocal对象，所以，它持有的数据库连接对于每个线程看到的都是不一样的。任何一个线程都无法访问到其他线程持有的数据库连接。

# 有了这两个全局变量，我们继续实现数据库连接的上下文，目的是自动获取和释放连接：

class _ConnectionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self

    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()

def connection():
    return _ConnectionCtx()

# 定义了__enter__()和__exit__()的对象可以用于with语句，确保任何情况下__exit__()方法可以被调用。

'''
把_ConnectionCtx的作用域作用到一个函数调用上，可以这么写：

with connection():
    do_some_db_operation()

但是更简单的写法是写个@decorator：

@with_connection
def do_some_db_operation():
    pass
'''

'''
注意到Connection对象是存储在_DbCtx这个threadlocal对象里的，因此，嵌套使用with connection()也没有问题。
_DbCtx永远检测当前是否已存在Connection，如果存在，直接使用，如果不存在，则打开一个新的Connection。
'''

'''
对于transaction也是类似的，with transaction()定义了一个数据库事务：

with db.transaction():
    db.select('...')
    db.update('...')
    db.update('...')

事务也可以嵌套，内层事务会自动合并到外层事务中，这种事务模型足够满足99%的需求。
事务嵌套比Connection嵌套复杂一点，因为事务嵌套需要计数，每遇到一层嵌套就+1，离开一层嵌套就-1，最后到0时提交事务：
'''
class _TransactionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should_close_conn = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_close_conn = True
        _db_ctx.transactions = _db_ctx.transactions + 1
        return self

    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        _db_ctx.transactions = _db_ctx.transactions - 1
        try:
            if _db_ctx.transactions==0:
                if exctype is None:
                    self.commit()
                else:
                    self.rollback()
        finally:
            if self.should_close_conn:
                _db_ctx.cleanup()

    def commit(self):
        global _db_ctx
        try:
            _db_ctx.connection.commit()
        except:
            _db_ctx.connection.rollback()
            raise

    def rollback(self):
        global _db_ctx
        _db_ctx.connection.rollback()

# 最后，把select()和update()方法实现了，db模块就完成了。





