import tkinter as tk
import sys
from timeit import default_timer as timer
import time
from PIL import ImageTk, Image



tot_time=0
del_time=0
imgpath=r'logo.jpg'

def NewTab():
    start=timer()
    time.sleep(del_time) #user defined delay time
    window.withdraw()
    win2.deiconify()
    end=timer()
    tot_time=end-start

    labW2.configure(text=('That took %s miliseconds or %s seconds'%(str(round(tot_time*1000,5)),str(round(tot_time,5)))))

def close():
    sys.exit()

def NTButt():
    win2.withdraw()
    window.deiconify()


win2=tk.Tk()
win2.geometry('1100x900')
win2.title('Button Click')
labW2=tk.Label(win2, text='ERROR: Time could not be calculated')
butW2=tk.Button(win2, text='Go back', bg='White', command=NTButt)
btn2W2=tk.Button(win2, text='Leave', bg='Red', command=close)
labW2.pack()
butW2.pack()
btn2W2.pack()
win2.withdraw()



window=tk.Tk()
window.geometry('1100x900')
window.title('Hello World')
lab1= tk.Label(window, text='Input the desired delay time')
ent=tk.Entry(window)
btn=tk.Button(window, text='Go to new window', bg='Blue', command=NewTab)
btn2=tk.Button(window, text='Leave', bg='Red', command=close)
###############################################
imgset=ImageTk.PhotoImage(Image.open(imgpath))
photo = ImageTk.PhotoImage(imgset) 
labimg = tk.Label(window, image=photo)
labimg.image = photo 
labimg.pack()
###############################################
lab1.pack()
ent.pack()
btn.pack()
btn2.pack()

window.mainloop()
