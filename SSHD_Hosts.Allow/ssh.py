#!/usr/bin/python
import os
from sys import argv
import  socket
import sqlite3

file2 = "/etc/hosts.allow"
file1 = "/etc/hosts.deny"


def list_allowing_ip():

	print os.system('cat '+file2+' ')

def list_blooking_ip():

	print os.system('cat '+file1+' ')


def AddToAllow(address):
	os.system("echo -n  "+data+" >> "+file2)
	print "SUCCESS"

def AddToDeny(address):
	data = " %s"
	os.system("echo -n  "+data+" >> "+file1)
	print "SUCCESS"

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  
        return False

    return True

def main():
	if (argv[1].upper() == "LIST2"):
		list_allowing_ip()
	
	elif(argv[1].upper()  == "LIST1"):
		list_blooking_ip()

	elif(is_valid_ipv4_address(argv[1])):
		if(argv[2].upper() == "ENABLE"):
			enable_ip(argv[1])
		elif(argv[2].upper() == "DISABLE"):
			disable_ip(argv[1])

	
if __name__ == '__main__':
	main()

