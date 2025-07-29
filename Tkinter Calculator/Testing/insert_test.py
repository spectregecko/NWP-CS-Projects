from tkinter import *

def add_text(event):
    e.insert(e.index(INSERT), 2)

master = Tk()

test = DoubleVar()
e = Entry(master, textvariable=test)

e.grid(column=0,row=0)

test.set(0)

master.bind('<Return>', add_text)

master.mainloop()