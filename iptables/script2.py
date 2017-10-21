#!/usr/bin/python
import os
from sys import argv
import  socket 



file = "BlackList.ip"


def Free_system():
	os.system("iptables -F")
	os.system("echo >  "+file+" ") 
	return True

def Block_ip(address):
	mbr = 0
	wite_list = open(file, 'r')
	for ip in wite_list:
		if (address in ip):
			print "the %s alredy in Blocklist" % address
			mbr = 1
			break
			
	wite_list.close()
	if (mbr == 0 ):
		os.system("iptables -A INPUT -s "+ address +"  -j DROP") 
		os.system("echo "+ address +" >> BlackList.ip")
		print "SUCCESS"



def UnBlock_ip(address):
	ip = os.popen("more "+file+" |grep -o "+address+"", 'r').read()
	if (address not in ip):
		print "the %s  in not in white list" % address
	else:
		os.system("iptables -D INPUT -s "+ address +"  -j DROP") 
		ins = open(file).read()
    		out = open(file, 'w')
		
		ins = ins.replace(address, "")
		out.write(ins)
		out.close()		
		print "SUCCESS"
		#os.system("sed 's/%s/0/g' %s") % (address, file)

def list_allowing_ip():

	wite_list = open(file, 'r')
	for line in wite_list:
		print  line
	wite_list.close()


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
	if (len(argv) == 1):
		print"|*****************************************************************************|"
		print"| use  xxx.xxx.xxx.xxx  enable            [to enable ip address]              |"
		print"| use  XXX.XXX.XXX.XXX  disable           [to remove ip from white list]       |"
		print"| use  list                               [to print list of white list ip]     |"
		print"| use  free                               [to free the system]                |"
		print"|                                                                             |"
		print"|*****************************************************************************|"
	elif(argv[1].upper() == "HELP"):
		print"|*****************************************************************************|"
		print"| use  xxx.xxx.xxx.xxx  enable            [to enable ip address]              |"
		print"| use  XXX.XXX.XXX.XXX  disable           [to remove ip from white list]       |"
		print"| use  list                               [to print list of white list ip]     |"
		print"| use  free                               [to free the system]                |"
		print"|                                                                             |"
		print"|*****************************************************************************|"

	elif(argv[1].upper()  == "LIST"):
		list_allowing_ip()
	elif(argv[1].upper() == "FREE"):
		Free_system()
		print "SUCCESS"
	elif(is_valid_ipv4_address(argv[1])):
		if(argv[2].upper() == "BLOCK"):
			Block_ip(argv[1])
		elif(argv[2].upper() == "UNBLOCK"):
			UnBlock_ip(argv[1])

		else:
			print "\n\t ERROR IN THE ACTION \n"
			print "\t use (enable)   to block ip address \n"
			print "\t use (disable) to unblock ip address\n"
			print "\t use (list)    to list all blocking ip "
	else:
		print "/n/t plise enter valied ip adress /n/n"

if __name__ == '__main__':
	main()

