#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用web框架示例

# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来

# First run, reports: no module named flask
# Solution:  Preferences-> Project -> Project Interpreter -> add "install flask"
from flask import Flask
from flask import request

# 把当前进程与flask关联在一起
app = Flask(__name__)

# 分别映射网址与处理函数
# 处理3个url:
# 1. GET /: 首页, 返回"Home Page"
# 2. GET /signin: 登陆页, 显示登陆表单
# 3. POST /signin: 处理登录表单, 显示登录结果
#
# 需要注意的是:
# 同一个URL: /signin分别有GET和POST两种请求, 分别映射到两个处理函数中

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home Page</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/baochen',methods=['GET'])
def hello():
    return '<h1>Hello, Baochen ! </h1>'

if __name__ == '__main__':
    app.run()

'''
除了Flask，常见的Python Web框架还有：

Django：全能型Web框架；

web.py：一个小巧的Web框架；

Bottle：和Flask类似的Web框架；

Tornado：Facebook的开源异步Web框架。
'''