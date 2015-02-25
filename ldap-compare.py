#!/usr/bin/python
# -*- coding: utf-8 -*-
# Compare DNS/DHCP of two Univention UCS 2.3 vs UCS 3.0
# Search for duplicity
#
# Example:
# dn: cn=igel5,cn=Sottrum,cn=computers,dc=jugendhilfe-wuemmetal,dc=de
# aRecord: 192.168.4.116
# cn: igel5
# macAddress: 00:e0:c5:5f:75:05

# (c) 2013 by Klaus Kappel <kkappel@jugendhilfe-wuemmetal.de>

import ldap
import socket
import webbrowser

def iptoint(ip):
    return int(socket.inet_aton(ip).encode('hex'),16)

def inttoip(ip):
    return socket.inet_ntoa(hex(ip)[2:].zfill(8).decode('hex'))


def get_ips(LDAPSERVER, base, domain): 
   ids = dict()
   ldapqry = '(objectclass=*)'
   ld = ldap.open(LDAPSERVER)
   l = ld.search_s(base, ldap.SCOPE_SUBTREE, filterstr=ldapqry)
   for i in l:
      for k in i[1]:
         if k == 'aRecord':
             kn = i[1]['cn'][0] + domain
             ids[kn] = iptoint(i[1]['aRecord'][0])
   return ids


if __name__ == "__main__":

   ucsmaster = get_ips('192.168.0.9', 'cn=computers,dc=jugendhilfe-wuemmetal,dc=de', '.jugendhilfe-wuemmetal.de')
   piaget = get_ips('192.168.0.5', 'cn=computers,dc=juhiwue,dc=de', '.juhiwue.de')
   alle = dict(ucsmaster, **piaget)
   oldip = 0
   f = open('/tmp/ips.txt','w')
   f.write('Alle IP`s in den Domains\n')
   for fqdn in sorted(alle, key=alle.get):
       if alle[fqdn] == oldip:
           f.write('doublette:')

       f.write(inttoip(alle[fqdn]) +'\t'+ fqdn +'\n')
       oldip = alle[fqdn]

   f.close()
   url = "file:///tmp/ips.txt"
   webbrowser.open(url,new=2)
