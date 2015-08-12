#!/usr/bin/python
#
#
# (c) 2015 by Klaus Kappel

import dns.query
import dns.zone
from socket import inet_aton
import struct

qry = (('192.168.0.5','juhiwue.de'),('192.168.0.9','jugendhilfe-wuemmetal.de'))

ips = []

for q in qry:

    z = dns.zone.from_xfr(dns.query.xfr(q[0], q[1]))
    names = z.nodes.keys()
    names.sort()
    for n in names:
        z0 = z[n].to_text(n)
        r = z0.split(' ')
        if r[3] == 'A':
            ips.append((r[4], r[0] +'.'+ q[1]))

#ips.sort()


sips = sorted(ips, key=lambda line: struct.unpack("!L", inet_aton(line[0])))

for i in sips:
   print i[0], i[1]
	      
