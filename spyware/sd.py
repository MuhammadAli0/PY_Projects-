#!/usr/bin/env python
from scapy.all import *
a = sniff(iface="wlp18s0", filter="tcp and port 80", count=10)
print a
