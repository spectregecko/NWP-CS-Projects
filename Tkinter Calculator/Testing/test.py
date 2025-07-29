
from tkinter import *

def launch():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    top.attributes('-topmost', 'true')
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()
 
root = Tk()
root.geometry("200x300")
root.title("main")
 
l = Label(root, text = "This is root window")
l.pack()
b = Button(root, text='Click Me!', command=launch)
b.pack()
 

 
root.mainloop()