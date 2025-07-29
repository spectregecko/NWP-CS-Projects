from tkinter import *
from tkinter import ttk
import math

def show_sin():
    # create the coordinate list for the sin() curve, have to be integers
    xy1 = []
    for x in range(400):
        # x coordinates
        xy1.append(x * x_increment)
        # y coordinates
        xy1.append(int(math.sin(x * x_factor) * y_amplitude) + center)
    return c.create_line(xy1, fill='blue')

def show_cos():
    xy2 = []
    for x in range(400):
        # x coordinates
        xy2.append(x * x_increment)
        # y coordinates
        xy2.append(int(math.cos(x * x_factor) * y_amplitude) + center)
    return c.create_line(xy2, fill='red')

def show_tan():
    xy3 = []
    for x in range(400):
        # x coordinates
        xy3.append(x * x_increment)
        # y coordinates
        xy3.append(int(math.tan(x * x_factor) * y_amplitude) + center)
    return c.create_line(xy3, fill='green')

def delete_line(line):
    c.delete(line)

def check_vars():
    print(toggle_sin.get())
    print(toggle_cos.get())
    print(toggle_tan.get())

root = Tk()
root.geometry("600x600")
root.title("Simple plot using canvas and line")

choice = StringVar()
choice.set('Simple Functions')
mode_chosen = ttk.Combobox(root, width=27, textvariable=choice)
mode_chosen['values'] = ('Simple Functions','Trigonometric Functions')
# mode_chosen.current()
mode_chosen.pack()

width = 400
height = 300
center = height//2
x_increment = 1
# width stretch
x_factor = 0.04
# height stretch
y_amplitude = -80

c = Canvas(width=width, height=height, bg='white')
c.pack(pady=20)

str1 = "sin(x)=blue"
c.create_text(10, 20, anchor=SW, text=str1)

center_line = c.create_line(0, center, width, center, fill='black')

# https://stackoverflow.com/questions/27397091/how-to-draw-sinus-wave-with-tkinter

function_menu = Menubutton(root, text='Functions', relief=RAISED)
# function_menu.grid()
function_menu.menu = Menu(function_menu, tearoff=0)
function_menu['menu'] = function_menu.menu

toggle_sin = BooleanVar()
toggle_cos = BooleanVar()
toggle_tan = BooleanVar()

function_menu.menu.add_checkbutton(label='Sin(x)', variable=toggle_sin)
function_menu.menu.add_checkbutton(label='Cos(x)', variable=toggle_cos)
function_menu.menu.add_checkbutton(label='Tan(x)', variable=toggle_tan)
function_menu.pack()

check_vars()

sin_line = show_sin()
cos_line = show_cos()
tan_line = show_tan()

x0 = [i for i in range(400)]
y0 = [i for i in range(400)]
y_equals_x_line = []
for i in range(400):
    y_equals_x_line.append(x0[i])
    y_equals_x_line.append(y0[i])
y_x_line = c.create_line(y_equals_x_line, fill='gray')

delete_sin = Button(root, text='Delete Sin', command=lambda: delete_line(sin_line))
delete_cos = Button(root, text='Delete Cos', command=lambda: delete_line(cos_line))
delete_tan = Button(root, text='Delete Tan', command=lambda: delete_line(tan_line))
delete_sin.pack()
delete_cos.pack()
delete_tan.pack()

user_x = IntVar()

attributes = LabelFrame(root, text='Attributes')
modify_x = Spinbox(attributes, textvariable=user_x, from_=-10, to=10).grid(column=0, row=0)
attributes.pack()

# refresh = Button(root, text='Refresh', command=refresh_graph)
# refresh.pack()

root.mainloop()