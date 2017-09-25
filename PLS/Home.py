from Tkinter import *
import time

def start():
    m1 = 0
    b1.destroy()
    while (m1 <= 60):
        app.update()
        time.sleep(1)
        m1= m1 +1
        start_time1.config(text=("%d") % (m1))


def stop():

    return

app = Tk()
app.title("HOME")
Label(app, text="|PS TITLE|", fg="black", bg="white").grid(row=0, column=0, sticky=W)
Label(app, text="|START TIME|", fg="black", bg="white").grid(row=0, column=1, sticky=W)
Label(app, text="|STOPED TIME|", fg="black", bg="white").grid(row=0, column=2, sticky=W)
Label(app, text="|CLEARD TIME|", fg="black", bg="white").grid(row=0, column=3, sticky=W)
Label(app, text="|BOUNTY $|", fg="black", bg="white").grid(row=0, column=4, sticky=W)

Label(app, text="|PS 1|", bg="blue", fg="white").grid(row=1, column=0, sticky=W)
Label(app, text="|PS 2|", bg="blue", fg="white").grid(row=2, column=0, sticky=W)
Label(app, text="|PS 3|", bg="blue", fg="white").grid(row=3, column=0, sticky=W)
Label(app, text="|PS 4|", bg="blue", fg="white").grid(row=4, column=0, sticky=W)
Label(app, text="|PS 5|", bg="blue", fg="white").grid(row=5, column=0, sticky=W)




start_time1 = Label(app,  bg="blue", fg="white")
start_time1.grid(row=1, column=1, sticky=W)

start_time2 = Label(app,  bg="blue", fg="white").grid(row=2, column=1, sticky=W)
start_time3 = Label(app,  bg="blue", fg="white").grid(row=3, column=1, sticky=W)
start_time4 = Label(app,  bg="blue", fg="white").grid(row=4, column=1, sticky=W)
start_time5 = Label(app,  bg="blue", fg="white").grid(row=5, column=1, sticky=W)



Stoped_time1 = Label(app,  bg="blue", fg="white").grid(row=1, column=2, sticky=W)
Stoped_time2 = Label(app,  bg="blue", fg="white").grid(row=2, column=2, sticky=W)
Stoped_time3 = Label(app,  bg="blue", fg="white").grid(row=3, column=2, sticky=W)
Stoped_time4 = Label(app,  bg="blue", fg="white").grid(row=4, column=2, sticky=W)
Stoped_time5 = Label(app,  bg="blue", fg="white").grid(row=5, column=2, sticky=W)

time1 = ''

# def start():
#     m = 0
#     s = 0
#     start_time1.config(text=("%d:%d") % (m, s))
#     start_time1.after(200, start)
#     while(m <= 60):
#         start_time1.config(text=("%d:%d")%(m, s))
#         start_time1.after(200, start)
#         time.sleep(1)
#         s = s + 1
#         if s == 60:
#             m = m + 1
#             s = 0
#
#
#     # global time1
#     # # get the current local time from the PC
#     # time2 = time.strftime('%H:%M:%S')
#     # # if time string has changed, update it
#     # if time2 != time1:
#     #     time1 = time2
#     #     start_time1.config(text=time1)
#     # # calls itself every 200 milliseconds
#     # # to update the time display as needed
#     # # could use >200 ms, but display gets jerky
#     # start_time1.after(200, start)


b1 = Button(app, text="START", command=start)
b1.grid(row=1, column=5, sticky=W)

Button(app, text="STOP", command=stop).grid(row=1, column=6, sticky=W)

Button(app, text="START", command=start).grid(row=2, column=5, sticky=W)
Button(app, text="STOP", command=stop).grid(row=2, column=6, sticky=W)

Button(app, text="START", command=start).grid(row=3, column=5, sticky=W)
Button(app, text="STOP", command=stop).grid(row=3, column=6, sticky=W)

Button(app, text="START", command=start).grid(row=4, column=5, sticky=W)
Button(app, text="STOP", command=stop).grid(row=4, column=6, sticky=W)

Button(app, text="START", command=start).grid(row=5, column=5, sticky=W)
Button(app, text="STOP", command=stop).grid(row=5, column=6, sticky=W)









Button(app, text="Exit", fg='blue', bg='red', command=app.destroy).grid(row=10, column=0, sticky=W)
app.mainloop()
