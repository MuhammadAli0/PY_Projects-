from tkinter import *

def avance(gd, hb):
	global x1, y1
	x1, y1 = x1 +gd, y1 +hb
	can1.coords(oval1, x1, y1, x1+30, y1+30)

def depl_gauche():
	avance(-10, 0)

def depl_droite():
	avance(10, 0)

def depl_haut():
	avance(0, -10)

def depl_bas():
	avance(0, 10)


x1, y1= 10, 10
fen1 = Tk()
fen1.title("Exrecice d' animation avec tkinter")
can1 = Canvas(fen1, bg='dark grey', height=300, width=300)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
can1.pack(side=LEFT)
Button(fen1, text='Quitter', command=fen1.quit).pack(side=BOTTOM)
Button(fen1, text='Gauche', command=depl_gauche).pack()
Button(fen1, text='Droite', command=depl_droite).pack()
Button(fen1, text='bas', command=depl_bas).pack()
Button(fen1, text='Haut', command=depl_haut).pack()

fen1.mainloop()
