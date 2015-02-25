#!/usr/bin/python

import socket, IN

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hostName = 'carl.wuemmetal.de'
PORT = 9999
s.connect((hostName, PORT))
s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
try:
    s.send('#' * 1473)
except socket.error:
    print 'The message did not make it'
    option = getattr(IN, 'IP_MTU', 14)
    print 'MTU:', s.getsockopt(socket.IPPROTO_IP, option)
else:
    print 'The big message was sent! Your network supports really big packets!'
