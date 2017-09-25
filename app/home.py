# -*- coding: UTF-8 -*-

from Tkinter import *
from L2  import *


app = Tk()
app.geometry('1200x800')
app.title("القائمه الرئيسيه")

msg = Message(app, bg="red",justify='left', text="اهلا")
msg.config(font=('times', 72, 'bold'))
msg.pack(fill=BOTH, side=TOP)



Button(app, width=40, bg='blue', text='REPORT', command=database).pack( side= RIGHT)
Button(app, width=40, bg='blue', text='SALER', command=database).pack( side= RIGHT)
Button(app, width=40, bg='blue', text='DATABASE', command=database).pack( side= RIGHT)
Button(app, width=40, bg='blue', text='STORGE', command=func).pack( side= RIGHT)
Button(app, width=40, bg='blue', text='exit', command=app.destroy).pack(side=BOTTOM)
app.mainloop()

