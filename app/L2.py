# -*- coding: UTF-8 -*-
from func import *
import socket
# -*- coding: UTF-8 -*-

from database import *
from Tkinter import *

def func():
    sss = Tk()
    sss.geometry("600x600")
    sss.title("المخزن")
    App(sss).pack(fill="both", expand=True)
    sss.mainloop()

def database():
    db = Tk()
    db.title("كل البضائع")
    Example(db).pack(fill="both", expand=True)
    db.mainloop()

def conec(server):
    conn = socket.create_connection(server)
    if conn.bind:
        respnse = conn.recv(1024)
        return respnse
    else:
        return False
def 


