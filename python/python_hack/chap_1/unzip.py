#/usr/bin/evn python
# -*- coding: utf-8 -*-

import zipfile
import os, time
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '\n[+] Successful!!!'
        print '[+] Password = [' + password + ']'
    except Exception, e:
        print '[-] Try: [' + password + '] failed ...'

def main():
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
