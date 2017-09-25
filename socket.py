#!/usr/bin python

import socket
sos=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sos.bind(("localhost",80))
sos.listen(5)
mysock,(raddr,rport)=sos.accept()
data=mysock.recv(1024)
mysock.send("<H1>Welcome to my Server</H1>")
sos.close()
