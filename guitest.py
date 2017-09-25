from tkinter import *

fen1 = Tk()
text1 = Label(fen1, text = 'Premier champ :')
text2 = Label(fen1, text = 'Second :')
entreal1 = Entry(fen1)
entreal2 = Entry(fen1)


can1 = Canvas(fen1, width = 160, height = 160, bg = 'white')
photo = PhotoImage(file = '/home/muhammad/Desktop/example.png')
item = can1.create_image(80, 80, image = photo)



text1.grid(row = 0)
text2.grid(row = 1)

entreal1.grid(row = 0, column = 1 )
entreal2.grid(row = 1, column = 1 )

fen1.mainloop()

