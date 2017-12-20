#/usr/bin/evn python
# -*- coding: utf-8 -*-

# 运行时可实时指定要破解的文件以及字典文件
# 增加参数解析功能

import zipfile
import os, time
import optparse

from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '\n[+] Successful!!!'
        print '[+] Password = [' + password + ']'
    except Exception, e:
        print '[-] Try: [' + password + '] failed ...'

def main():
    parser = optparse.OptionParser("usage %prog " +\
    "-f <zipfile> -d <dictionary>")

    parser.add_option('-f',dest='zname', type='string', \
    help='specity zip file')

    parser.add_option('-d',dest='dname', type='string', \
    help='specity dictionary file')

    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    # 如果当前目录下存在解压后的文件, 先删除
    if os.path.isfile('./evil.txt'):
        print '### ./evil.txt exists, remove it.'
        os.remove('./evil.txt')
        time.sleep(3)

    zFile = zipfile.ZipFile('./testfile/evil.zip')

    with open('./testfile/dictionary.txt') as passFile:
        for line in passFile.readlines():
            password = line.strip('\n')
            # result = extractFile(zFile,password)
            # 利用多线程提高破解效率
            t = Thread(target=extractFile, args=(zFile,password))
            t.start()

if __name__ == '__main__':
    main()
