#! /usr/bin/env python

import sys
import os
import socket
import re
import optparse

def tcp4_out(host, port):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.settimeout(2)
    # get ipv4 address
    r = 1
    try:
        ip = socket.gethostbyname(host)
        r = tcp.connect_ex((ip, port))
    except (socket.timeout, socket.error):
        pass
    tcp.close()
    if r == 0:
        return True
    return False

def tcp6_out(host, port):
    # not supported yet
    return False

def udp4_out(host, port):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.settimeout(2)
    r = ''
    try:
        udp.connect((host, port))
        udp.send('Hello!\n')
        r = udp.recv(15)
    except (socket.timeout, socket.error):
        pass
    if len(r) > 0:
        return True
    return False

def parseoptions():
    usage = "usage: %prog [options] <host> <port>"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('--protocol',
                      help='protocol: tcp4, tcp6, udp4',
                      action="store",
                      dest="protocol",
                      default="tcp4",
                      type="string")

    options,remainder = parser.parse_args()
    return options,remainder

if __name__=='__main__':

    options,remainder = parseoptions()

    fxn_lookup = {
        'tcp4' : tcp4_out,
        'tcp6' : tcp6_out,
        'udp4' : udp4_out
    }

    fxn = fxn_lookup[options.protocol]

    # should only be host and port left in the args list
    if (len(remainder) != 2):
        raise RuntimeError("Wrong # arguments, use --help for help")

    host,port = remainder
    result = 0

    port = int(port)
    if (port < 0) or (port > 65535):
        raise RuntimeError("Port must be between 0 and 65535")

    result = fxn(host,port)
    print >>sys.stdout, result

    sys.exit()
