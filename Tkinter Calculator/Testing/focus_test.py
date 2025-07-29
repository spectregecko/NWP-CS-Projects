from tkinter import *

def who_is_focused(event):
    print(main.focus_get())

main = Tk()
main.geometry('400x200')

entry1 = Entry(main)
entry2 = Entry(main)

entry1.pack()
entry2.pack()

main.bind('<Return>', who_is_focused)

main.mainloop()