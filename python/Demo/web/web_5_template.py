#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 访问方法:
# 127.0.0.1:5000/signin

# 使用MVC: Model - View - Controler 模式来区划清层级, 简化开发

# 一定要把模板放到正确的templates目录下，templates和本文件在同级目录下

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'] )
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def sigin():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password',username=username)

if __name__ == '__main__':
    app.run()