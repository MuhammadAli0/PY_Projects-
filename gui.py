from tkinter import *
from random import randrange

def drowline():
	global x1, y1, x2, y2, coul

	can1.create_line(x1, y1, x2, y2, width=2, fill = coul)
def changecolor():
	global coul
	pal=['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
	c = randrange(8)
	coul = pal[c]

x1, y1, x2, y2= 10, 190, 190, 10
coul = 'dark green'
fen1 = Tk()
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Trace une ligne', command = drowline)
bou2.pack()
bou3 = Button(fen1, text='Autre couleur', command = changecolor)
bou3.pack()
fen1.mainloop()
fen1.destroy()

