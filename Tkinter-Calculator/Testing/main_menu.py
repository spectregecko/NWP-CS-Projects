from tkinter import *
from calculator import *

def launch_calculator():
    #calculator.mainloop() # Runs the program.
    pass

main = Tk()
main.geometry('500x500')

b = Button(main, text='Click Me!', command=launch_calculator)
b.pack()

main.mainloop()




# main.mainloop()