#/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import string
#from socket import *
import socket
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send ('ViolentPython\r\n')
        result = connSkt.recv(100)
        screenLock.acquire()
        print '[+]%d/tcp open'  %tgtPort
        print '[+] Banner: ' + str(result)
    except:
        screenLock.acquire()
        print '[-]%d/tcp closed' %tgtPort
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print "[-] Cann't resolve '%s': Unknown Host" %tgtHost
        return

    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print '\n[+] Scan results for: ' + tgtName[0]
    except:
        print "\n[+] Scan results for: " + tgtIP
        reutrn

    socket.setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        t = Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('usage %prog ' + \
            '-H <target_host> -p <target_port>')
    parser.add_option('-H', dest='tgtHost', type='string', \
            help='specify target host')
    parser.add_option('-p', dest='tgtPorts', type='string', \
            help='specify target ports')
    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')

    '''
    pp = ['10','20','30']
    pp = 10,20,30
    for p in tgtPorts:
        print '%d' %int(p)

    exit(0)
    '''

    if(tgtHost == None ) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)

    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()

