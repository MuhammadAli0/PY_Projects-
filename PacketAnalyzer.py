#!/usr/bin/ python
import struct
import socket
import os
import binascii

def analyze_tcp_hdr(data):
    tcp_hdr  = struct.unpack('!2H2i4H', data[:20])
    src_port = tcp_hdr[0]
    dst_port = tcp_hdr[1]
    sequence = tcp_hdr[2]
    ackn     = tcp_hdr[3]
    offset   = tcp_hdr[4] >> 12
    reserved = (tcp_hdr[4] >> 6) & 0x03ff #must be zero
    flag     = tcp_hdr[4] & 0x003f
    URG      = flag & 0x0020
    ACK      = flag & 0x0010
    PSH      = flag & 0x0008
    RST      = flag & 0x0004
    SYN      = flag & 0x0002
    FIN      = flag & 0x0001
    windows  = tcp_hdr[5]
    checksum = tcp_hdr[6]
    uregent  = tcp_hdr[7]
    print "|********************************  TCP Header  ********************************|"
    print "|\Source Port: \t\t\t\t\t\t%s" % src_port
    print "|\Destination Port: \t\t\t\t\t%s" % dst_port
    print "|\Sequense: \t\t\t\t\t\t%s" % sequence
    print "|\Acknowlagment: \t\t\t\t\t%s" % ackn
    print "|\Offset: \t\t\t\t\t\t%s" % offset
    print "|\Reserved: \t\t\t\t\t\t%s" % reserved
    print "|\Flag: \t\t\t\t\t\t%s" % flag
    print "|\URG: \t\t\t\t\t\t\t%s" % URG
    print "|\Windows: \t\t\t\t\t\t%s" % windows
    print "|\Checksum: \t\t\t\t\t\t%s" % checksum
    print "|\Uregent: \t\t\t\t\t\t%s" % uregent
    jem  = {"ACK":ACK, "PSH":PSH, "RST":RST, "SYN":SYN, "FIN":FIN}
    for ja in jem:
        if jem[ja] != 0:
            print "|\%s" % ja + ":\t\t\t\t\t\t\t%d" % jem[ja]

    data     = data[20:]
    return data

def analyze_udp_hdr(data):
    udp_hdr     = struct.unpack('!4H', data[:8])
    src_port    = udp_hdr[0]
    dst_port    = udp_hdr[1]
    length      = udp_hdr[2]
    checksum    = udp_hdr[3]
    print "|********************************  UDP Header  *******************************|"
    print "|\Source Port: %s" %src_port
    print "|\Destination Port: %s" % dst_port
    print "|\Packet length: %s" % length
    print "|\Packet Checksum: %s" %  checksum
    data        = data[8:]
    return data

def analyze_ip_hdr(data):
    ip_hdr = struct.unpack('!6H4s4s', data[:20])
    ver         =  ip_hdr[0] >> 12          #run 12 bits
    ihl         = (ip_hdr[0] >> 0) & 0x0f   #00001111 & 01010101 = 00000101
    tos         = ip_hdr[0] & 0x00ff        #0000 0000 1111 1111
    tot_len     = ip_hdr[1]
    idntity     = ip_hdr[2]
    offcet      = ip_hdr[3] >> 13           #only the first 13 bit
    flags       = ip_hdr[3] &  0x1fff       #1110 =2+4+8=14
    ttl         = ip_hdr[4] >> 8
    proto       = ip_hdr[4] &  0x00ff
    hdr_sum     = ip_hdr[5]
    src_address = socket.inet_ntoa(ip_hdr[6])
    dst_address = socket.inet_ntoa(ip_hdr[7])
    print "|*********************************  IP Header  ********************************|"
    print "|\IPv: \t\t\t\t\t\t\t%d" % ver
    print "|\IHL: \t\t\t\t\t\t\t%d" % ihl
    print "|\TOS: \t\t\t\t\t\t\t%d" % tos
    print "|\Total Length: \t\t\t\t\t%d" % tot_len
    print "|\Indentity: \t\t\t\t\t\t%d" % idntity
    print "|\Checksum Offset:\t\t\t\t\t%d" % offcet
    print "|\Flags: \t\t\t\t\t\t%d" % flags
    print "|\TTL: \t\t\t\t\t\t\t%d" % ttl
    print "|\Proto:  \t\t\t\t\t\t%d" % proto
    print "|\Header Checksum: \t\t\t\t\t%d" % hdr_sum
    print "|\Sourse Address: \t\t\t\t\t%s" % src_address
    print "|\Destination Address: \t\t\t\t\t%s " % dst_address


    if proto  == 6:
        next_proto = "TCP"
    if proto == 17:
        next_proto = "UDP"

    data = data[20:]
    return data, next_proto

def analyze_ether(data):

    ip_bool     = False
    eth_hdr     = struct.unpack('!6s6sH' , data[:14]) #IPv4 = 0x0000
    dest_mac    = binascii.hexlify(eth_hdr[0])
    src_mack    = binascii.hexlify(eth_hdr[1])
    proto       = eth_hdr[2]

    if hex(proto) == "0x800" : # IPv4
        ip_bool = True

    print "|******************************  Ethernet Header  *****************************|"
    print "|\Destnation MAC: \t\t\t\t\t%s %s %s %s %s %s" % (dest_mac[0:2], dest_mac[2:4], dest_mac[4:6], dest_mac[6:8], dest_mac[8:10], dest_mac[10:12])
    print "|\Source MAC: \t\t\t\t\t\t%s %s %s %s %s %s" %  (src_mack[0:2], src_mack[2:4], src_mack[4:6], src_mack[6:8], src_mack[8:10], src_mack[10:12])
    print "|\PROTO:\t\t\t\t\t\t%s" % hex(proto)


    data = data [14:]
    return data, ip_bool

def main():
    sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    recive_data = sniffer_socket.recv(2048)
    os.system('clear')
    data, ip_bool = analyze_ether(recive_data)
    if ip_bool:
        data, next_proto = analyze_ip_hdr(data)
    else:
        return
    if next_proto == 'TCP':
        data = analyze_tcp_hdr(data)
    elif next_proto == 'UDP':
        data = analyze_udp_hdr(data)
    else:
        return

while True:
    main()