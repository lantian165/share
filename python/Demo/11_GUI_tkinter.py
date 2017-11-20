#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

# 从Frame派生一个Application类, 这是所有Widget的父容器
'''
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        self.size = ()
'''

'''
在GUI中, 每个Button, Label, 输入框等, 都是一个Widget.
Frame则是一个可以容纳其它Widget的Widget, 所有的Widget组合起来就是一颗树
pack()方法把Widget加入到父容器中, 并实现布局.pack()是最简单的布局.
grid()可以实现更复杂的布局.
'''

import tkMessageBox

# 改进版,增加文本框输入
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text='Click Me', command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name )

# 实例化 Application(), 并启动消息循环:
app = Application()

#设置主容器标题
app.master.title('Hello World')

# 主消息循环
app.mainloop()

