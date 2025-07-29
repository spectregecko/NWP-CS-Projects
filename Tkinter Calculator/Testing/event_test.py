from tkinter import Tk

def on_window_close(event):
    print('Window is closing...')

def on_mouse_click(event):
    print('Mouse clicked at:', event.x, ', ', event.y)

root = Tk()
root.title('Hello GUI!')
root.geometry('400x200+200+100')
root.configure(bg='blue')

root.bind('<Button-1>', on_mouse_click)
root.bind('<Destroy>', on_window_close)

root.mainloop()