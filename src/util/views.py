# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import re


def ipaddr_str_to_long(ipaddr_str):
    IPAddrRE = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')
    m = IPAddrRE.match(ipaddr_str)
    if not m: return 0
    oct1, oct2, oct3, oct4 = m.groups()
    oct1, oct2, oct3, oct4 = (int(oct1), int(oct2), int(oct3), int(oct4))
    return oct4 + (oct3 << 8) + (oct2 << 16) + (oct1 << 24)


def ipaddr_long_to_str(ipaddr_long):
    oct4 = ipaddr_long & 255
    ipaddr_long >>= 8
    oct3 = ipaddr_long & 255
    ipaddr_long >>= 8
    oct2 = ipaddr_long & 255
    ipaddr_long >>= 8
    oct1 = ipaddr_long & 255
    return '%d.%d.%d.%d' % (oct1, oct2, oct3, oct4)