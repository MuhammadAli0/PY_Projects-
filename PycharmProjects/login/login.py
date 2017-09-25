#!/usr/bin/env python

import base64

user = []
passwd = []

def registration():
    username = raw_input("USERNAME : ")
    password = base64.b64encode(raw_input("PASSWORD : "))
    print "yor detils after decript"

    user.append(username)
    passwd.append(password)
    print user, passwd

def login():
    username = raw_input("username : ")
    password = raw_input("Password : ")
    if username  in user and base64.b64encode(password) in passwd:
        print "Login Corect "

def main():
    print "enter registration details "
    registration()
    print "enter you login details"
    login()





if __name__=='__main__':
    main()