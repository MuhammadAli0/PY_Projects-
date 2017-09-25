from Tkinter import *
from ttk import *

# -*- coding: UTF-8 -*-

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky=(N, S, W, E))
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('starttime', 'endtime', 'status')
        tv.heading("#0", text='Sources', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('starttime', text='Start Time')
        tv.column('starttime', anchor='center', width=100)
        tv.heading('endtime', text='End Time')
        tv.column('endtime', anchor='center', width=100)
        tv.heading('status', text='Status')
        tv.column('status', anchor='center', width=100)
        tv.grid(sticky=(N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text="first", values=('10:00','10:10', 'Ok'))

    def but(self):
        Button(self, text='exit', fg="Red", command=sys.exit).grid(sticky=N,)
