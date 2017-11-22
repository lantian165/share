#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 写邮件 MUA: mail user agent 邮件客户端
# 发邮件 MTA: mail transfer agent 邮件传输代理: 新浪, 网易等
# 收邮件 MDA: mail delivery agent 邮件投递代理: 新浪, 网易等 (长期保留邮件, 待用户收取)

# 一封电子邮件的旅程:
# (发邮件)MUA -> MTA -> 若干个MTA -> MTA->MDA <- MUA(收邮件)

# 1. 发送邮件 MUA -> MTA
# 2. 接收邮件 MDA <- MUA

# 协议:
# 发邮件 SMTP
# 收邮件 POP3, IMAP(可直接操作MDA上的邮件)

# python 对SMTP支持有 smtplib和email两个模块, email负责构造邮件, smtplib负责发送邮件

# Part 1: 构造一个最简单的纯文本邮件
from email.mime.text import MIMEText
import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['Subject'] = 'Subject is: Python send mail'

# 这几个字段都是必填项, 不填写会报: 554 DT:SPM
# 邮件里显示的发件人, 收件人信息, 不是通过SMTP协议发送给MTA,
# 而是包含在MTA文本中, 必须把From, To, Subject添加到MIMEText中, 才是一封完整的邮件
msg['From'] = 'lantian165@163.com'
msg['to'] = 'wb-yebaochen@cai-inc.com'
msg['cc'] = 'lantian165@163.com'
content = '''
Hello, baochen
this is a mail send with python
If you see this msg, configurations!
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

# 第一个参数就是邮件正文, 第二个参数是MIME的subtype, 传入'plain', 最终的MIME就是'text/plain'
# 第三个参数用'utf-8'编码保证多语言的兼容性

# 通过smtp发送数据
from_addr = raw_input('From: ')
password  = raw_input('Password: ')

# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'  # raw_input('SMTP server: ')

# 输入收件人地址:
to_addr = raw_input('To: ')

server = smtplib.SMTP(smtp_server, 25) #SMTP协议端口默认是25
server.set_debuglevel(1)
server.login(from_addr,password)
# 可以一次发给多个人, 的以传入一个List
# 邮件正文是一个str, 用as_string()把MIMEText对象变成str
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
