from tkinter import *
from tkinter import messagebox

def open_calculator():
    pass

main = Tk()
main.title('Math Tools')
main.geometry('800x800')

mb = Menubutton(main, text='Tools', relief=RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb['menu'] = mb.menu

calculator = IntVar()
whiteboard = IntVar()

mb.menu.add_checkbutton(label='Calculator', variable=calculator)
mb.menu.add_checkbutton(label='Whiteboard', variable=whiteboard)

mb.pack()

main.mainloop()






#from calculator import root

