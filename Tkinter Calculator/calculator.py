from tkinter import *
from tkinter import ttk
from math import sin, cos, tan
from tkinter import messagebox
from fractions import Fraction # Allows us to represent floating-points as fractions.

DIVIDE   = 1
MULTIPLY = 2
ADD      = 3
SUBTRACT = 4

# Used for the focus_get function.
OPERAND_1 = '.!frame.!entry'
OPERAND_2 = '.!frame.!entry2'

FONT_1 = ('comic sans', 40)
FONT_2 = ('comic sans', 20)
FONT_3 = ('comic sans', 12)

def who_is_focused(event):
    """Prints out which Entry operand is focused. Used for testing purposes."""
    if str(calculator.focus_get()) == '.!frame.!entry':
        print('Operand 1')
    elif str(calculator.focus_get()) == '.!frame.!entry2':
        print('Operand 2')
    print(calculator.focus_get())

def on_window_close_request():
    """Asks the user if they are sure they want to close the calculator app."""
    if messagebox.askokcancel('Quit', 'Do you really wish to quit?'):
        calculator.destroy()

def change_operator():
    """Changes the operator label between the Entry operands."""
    if operator.get() == DIVIDE:
        current_op.set('÷')
    elif operator.get() == MULTIPLY:
        current_op.set('x')
    elif operator.get() == ADD:
        current_op.set('+')
    elif operator.get() == SUBTRACT:
        current_op.set('-')

def calculate_result():
    """Calculates the result of the current operation, with simple validation (i.e. check for divide by zero)."""
    if operator.get() == DIVIDE:
        if operand_2.get() == 0:
            raise ZeroDivisionError # Handled in the get_result function.
        return operand_1.get() / operand_2.get()
    elif operator.get() == MULTIPLY:
        return operand_1.get() * operand_2.get()
    elif operator.get() == ADD:
        return operand_1.get() + operand_2.get()
    elif operator.get() == SUBTRACT:
        return operand_1.get() - operand_2.get()

def get_result(event=None):
    """Sets the result Entry with the calculated result as either a fraction or rounded decimal, if both operands are filled."""
    global history_window
    try:
        answer = calculate_result()
        if fraction_mode.get() == True and not (operator.get() == DIVIDE and operand_2.get() == 0):
            result.set(str(Fraction(answer).limit_denominator()))
        else:
            result.set(str(format(answer, '.4g')))
        if history_window is not None:
            show_history()
        status.set('Successful Operation')
    except ZeroDivisionError:
        messagebox.showwarning(title='Division by 0', message='You cannot divide by zero!')
        status.set('Failed Operation')
        result.set('ERR')
    except Exception:
        messagebox.showwarning(title='Invalid Operation', message='This operation is invalid!')
        status.set('Failed Operation')
        result.set('')
    finally:
        status_message.pack_forget()
        status_message.pack()

def insert_number(value):
    """Inserts a number where the cursor is. The number inserted corresponds to what number was clicked on the keypad UI."""
    if str(calculator.focus_get()) == OPERAND_1:
        operand_1_input.insert(operand_1_input.index(INSERT), value)
    elif str(calculator.focus_get()) == OPERAND_2:
        operand_2_input.insert(operand_2_input.index(INSERT), value)

def delete_character():
    """Deletes the character left of the cursor."""
    if str(calculator.focus_get()) == OPERAND_1:
        operand_1_input.delete(operand_1_input.index(INSERT) - 1)
    elif str(calculator.focus_get()) == OPERAND_2:
        operand_2_input.delete(operand_2_input.index(INSERT) - 1)

def clear_entries():
    """Clears all the entries in the calculator."""
    operand_1.set('')
    operand_2.set('')
    result   .set('')
    status_message.pack_forget()

def show_history():
    """Opens a history window containing the last calculation the user did, and keeping this window open will make the history grow."""
    global history_window
    if history_window is None:
        open_history['state'] = 'disabled'
        history_window = Toplevel()
        history_window.title("History")
        # history_window.attributes('-topmost', 'true')
    history = Text(history_window, font=FONT_3, width=25, height=1)
    try:
        history.insert(history.index(INSERT), f'{operand_1.get()} {current_op.get()} {operand_2.get()} = {result.get()}')
    except Exception:
        pass
    history.pack()
    history_window.protocol('WM_DELETE_WINDOW', hide_history)

def hide_history():
    """Hides and clears the history window."""
    global history_window
    history_window.destroy()
    history_window = None
    open_history['state'] = 'normal'

def show_graph():
    """Opens a graph window that contains options to view and modify simple and trigonometric functions."""
    global graph_window
    if graph_window is None:
        # Sets up the graph window.
        open_graph['state'] = 'disabled'
        graph_window = Toplevel()
        graph_window.geometry('600x810')
        graph_window.title("Graph")
        graph_window.config(bg='gray20')
        # graph_window.attributes('-topmost', 'true')

        def graph_cycle(event):
            """Cycles between the trigonometric functions and the simple functions, depending on the chosen mode."""
            global graph_window
            if choice.get() == 'Trigonometric Functions':
                graph_window.destroy()
                graph_window = Toplevel()
                graph_window.geometry('600x810')
                graph_window.title("Graph")
                graph_window.config(bg='gray20')
                # graph_window.attributes('-topmost', 'true')
                trig_graph()
            elif choice.get() == 'Simple Functions':
                graph_window.destroy()
                graph_window = Toplevel()
                graph_window.geometry('600x810')
                graph_window.title("Graph")
                graph_window.config(bg='gray20')
                # graph_window.attributes('-topmost', 'true')
                simple_graph()    

        def trig_graph():
            """Shows the window that graphs trigonometric functions."""
            global choice
            mode_chosen = ttk.Combobox(graph_window, width=27, textvariable=choice)
            mode_chosen['values'] = ('Simple Functions','Trigonometric Functions')
            mode_chosen.pack(pady=20) 
            
            mode_chosen.bind('<<ComboboxSelected>>', graph_cycle)

            # Trigonometric functions inspired by https://stackoverflow.com/questions/27397091/how-to-draw-sinus-wave-with-tkinter.
            width = 400
            height = 300
            center = height//2
            x_increment = 1
            # width stretch
            x_factor = 0.04
            # height stretch
            y_amplitude = -40

            # Factors to be multiplied to the trigonometric functions for graph manipulation.
            a_factor = IntVar()
            a_factor.set(1)
            b_factor = IntVar()
            b_factor.set(1)
            c_factor = IntVar()
            c_factor.set(0)

            def show_trig(func, colour):
                """Draws the corresponding trig function on the canvas graph."""
                trig_placement = 1
                if c_factor.get() == 1: # These values are used to simulate moving the trig line up and down by 1. They were determined by trial and error.
                    trig_placement = 0.74
                elif c_factor.get() == -1:
                    trig_placement = 1.26
                # Create the coordinate list for the trigonometric function curve. They have to be integers.
                xy = []
                for x in range(width):
                    # X coordinates.
                    xy.append(x * x_increment)
                    # Y coordinates.
                    xy.append(a_factor.get() * int(func(x * x_factor * b_factor.get()) * y_amplitude) + (center * trig_placement))
                c.create_line(xy, fill=colour)
            
            # The legend above the graph.
            legend = Listbox(graph_window, width=15, height=4, font=FONT_3, bg='gray10', fg='white')
            legend.insert(1, 'Legend')
            legend.insert(2, 'a*sin(b*x)+c=red')
            legend.insert(3, 'a*cos(b*x)+c=blue')
            legend.insert(4, 'a*tan(b*x)+c=green')
            legend.pack()

            # The graph, showing all trigonometric functions by default.
            c = Canvas(graph_window, width=width, height=height, bg='white')
            c.pack(pady=20)
            c.create_line(0, center, width, center, fill='black')
            show_trig(sin,'red')
            show_trig(cos,'blue')
            show_trig(tan,'green')

            # The progress bar for when the user manipulates the attributes and refreshes the graph.
            progress_bar = ttk.Progressbar(graph_window, orient=HORIZONTAL, length=195, mode='determinate', variable=progress) 
            def refresh_graphs():
                """Refreshes the graphs with the new attributes."""
                current_progress = progress.get()
                progress_bar.pack()
                if current_progress < 100:
                    progress.set(current_progress + 1)
                    graph_window.after(1, refresh_graphs)
                else:
                    progress_bar.pack_forget()
                    progress.set(0)
                    c.delete('all')
                    c.create_line(0, center, width, center, fill='black')
                    if toggle_sin.get() == True:
                        show_trig(sin,'red')
                    if toggle_cos.get() == True:
                        show_trig(cos,'blue')
                    if toggle_tan.get() == True:
                        show_trig(tan,'green')
            
            # The attributes that the user can manipulate.
            attributes = LabelFrame(graph_window, text='Attributes', bg='gray10', fg='white', font=FONT_3)
            a_text = Label(attributes, text='a factor', bg='gray10', fg='white', font=FONT_3).grid(column=0, row=0)
            modify_a = Spinbox(attributes, textvariable=a_factor, from_=1, to=5).grid(column=1, row=0)
            b_text = Label(attributes, text='b factor', bg='gray10', fg='white', font=FONT_3).grid(column=0, row=1)
            modify_b = Spinbox(attributes, textvariable=b_factor, from_=1, to=10).grid(column=1, row=1)
            c_text = Label(attributes, text='c factor', bg='gray10', fg='white', font=FONT_3).grid(column=0, row=2)
            modify_c = Scale(attributes, variable=c_factor, from_=1, to=-1, length=50, bg='gray10', fg='white', activebackground='yellow', highlightthickness=0).grid(column=1, row=2)
            attributes.pack()

            # The function menu (for showing and hiding) and the refresh button.
            bottom = Frame(graph_window, bg='gray20')
            function_menu = Menubutton(bottom, text='Show', bg='gray10', fg='white', relief=RAISED)
            function_menu.menu = Menu(function_menu, tearoff=0)
            function_menu['menu'] = function_menu.menu
            global toggle_sin
            global toggle_cos
            global toggle_tan
            function_menu.menu.add_checkbutton(label='sin(x)', variable=toggle_sin)
            function_menu.menu.add_checkbutton(label='cos(x)', variable=toggle_cos)
            function_menu.menu.add_checkbutton(label='tan(x)', variable=toggle_tan)
            function_menu.grid(column=0, row=0)
            refresh = Button(bottom, text='Refresh', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', highlightcolor='yellow', command=refresh_graphs)
            refresh.grid(column=1, row=0, padx=(10,0))
            bottom.pack(pady=20)

            graph_window.protocol('WM_DELETE_WINDOW', hide_graph)

        def simple_graph():
            """Shows the window that graphs simple functions."""
            global choice
            mode_chosen = ttk.Combobox(graph_window, width=27, textvariable=choice)
            mode_chosen['values'] = ('Simple Functions','Trigonometric Functions')
            mode_chosen.pack(pady=20) 
            
            mode_chosen.bind('<<ComboboxSelected>>', graph_cycle)

            width = 400
            height = 300
            center_1 = width//2
            center_2 = height//2

            # Factor to be multiplied to the simple functions.
            a_factor = IntVar()
            a_factor.set(1)

            # The legend above the graph.
            legend = Listbox(graph_window, width=13, height=4, font=FONT_3, bg='gray10', fg='white')
            legend.insert(1, 'Legend')
            legend.insert(2, '(1/a)*x=red')
            legend.insert(3, '(1/a)*x^2=blue')
            legend.insert(4, '(1/a)*x^3=green')
            legend.pack()

            # The graph, showing all simple functions by default.
            c = Canvas(graph_window, width=width, height=height, bg='white')
            c.pack(pady=20)
            c.create_line(0, center_2, width, center_2, fill='black')
            c.create_line(center_1, 0, center_1, height, fill='black')

            def line(): # Trial and error.
                """Draws the x function on the graph."""
                xy = []
                for x in range(width):
                    # X coordinates.
                    xy.append(x)
                    # Y coordinates.
                    xy.append(center_2 - (x - center_1)/((4/3)*a_factor.get()))
                c.create_line(xy, fill='red')
            line()
            
            def squared(): # Trial and error.
                """Draws the x^2 function on the graph."""
                xy = []
                for x in range(width):
                    # X coordinates.
                    xy.append(x)
                    # Y coordinates.
                    xy.append(center_2 - ((x - center_1)/(4 * a_factor.get()))**2)
                c.create_line(xy, fill='blue')
            squared()

            def cubed(): # Trial and error.
                """Draws the x^3 function on the graph."""
                xy = []
                for x in range(width):
                    # X coordinates.
                    xy.append(x)
                    # Y coordinates.
                    xy.append(center_2 - ((x - center_1)/(4 * a_factor.get()))**3)
                c.create_line(xy, fill='green')
            cubed()

            # The progress bar for when the user manipulates the attributes and refreshes the graph.
            progress_bar = ttk.Progressbar(graph_window, orient=HORIZONTAL, length=195, mode='determinate', variable=progress) 
            def refresh_graphs():
                """Refreshes the graphs with the new attributes."""
                current_progress = progress.get()
                progress_bar.pack()
                if current_progress < 100:
                    progress.set(current_progress + 1)
                    graph_window.after(1, refresh_graphs)
                else:
                    progress_bar.pack_forget()
                    progress.set(0)
                    c.delete('all')
                    c.create_line(0, center_2, width, center_2, fill='black')
                    c.create_line(center_1, 0, center_1, height, fill='black')
                    if toggle_line.get() == True:
                        line()
                    if toggle_squared.get() == True:
                        squared()
                    if toggle_cubed.get() == True:
                        cubed()

            # The attributes that the user can manipulate.
            attributes = LabelFrame(graph_window, text='Attributes', bg='gray10', fg='white', font=FONT_3)
            a_text = Label(attributes, text='a factor', bg='gray10', fg='white', font=FONT_3).grid(column=0, row=0, sticky=S)
            modify_a = Scale(attributes, variable=a_factor, from_=1, to=10, orient=HORIZONTAL, length=100, bg='gray10', fg='white', activebackground='yellow', highlightthickness=0).grid(column=1, row=0)
            attributes.pack()

            # The function menu (for showing and hiding) and the refresh button.
            bottom = Frame(graph_window, bg='gray20')
            function_menu = Menubutton(bottom, text='Show', bg='gray10', fg='white', relief=RAISED)
            function_menu.menu = Menu(function_menu, tearoff=0)
            function_menu['menu'] = function_menu.menu
            global toggle_line
            global toggle_squared
            global toggle_cubed
            function_menu.menu.add_checkbutton(label='x', variable=toggle_line)
            function_menu.menu.add_checkbutton(label='x^2', variable=toggle_squared)
            function_menu.menu.add_checkbutton(label='x^3', variable=toggle_cubed)
            function_menu.grid(column=0, row=0)
            refresh = Button(bottom, text='Refresh', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', highlightcolor='yellow', command=refresh_graphs)
            refresh.grid(column=1, row=0, padx=(10,0))
            bottom.pack(pady=20)

            graph_window.protocol('WM_DELETE_WINDOW', hide_graph)
        
        simple_graph()

def hide_graph():
    """Hides and clears the graph window."""
    global graph_window
    graph_window.destroy()
    graph_window = None
    open_graph['state'] = 'normal'

history_window = None
graph_window   = None

# Sets up the calculator window.
calculator = Tk()
# calculator.attributes('-topmost', 'true') # Keeps window above everything. For testing purposes.
calculator.geometry('600x810')
calculator.title('Calculator')
calculator.config(bg='gray20')

# Variables for the graph portion of the calculator.
choice         = StringVar()
toggle_line    = BooleanVar()
toggle_squared = BooleanVar()
toggle_cubed   = BooleanVar()
toggle_sin     = BooleanVar()
toggle_cos     = BooleanVar()
toggle_tan     = BooleanVar()
progress       = IntVar()
choice        .set('Simple Functions')
toggle_line   .set(True)
toggle_squared.set(True)
toggle_cubed  .set(True)
toggle_sin    .set(True)
toggle_cos    .set(True)
toggle_tan    .set(True)
progress      .set(0)

# Variables for the top of the calculator. These variables are used by their corresponding Entry and Label.
operand_1  = DoubleVar()
current_op = StringVar()
operand_2  = DoubleVar()
result     = StringVar()
operand_1 .set('')
current_op.set('+')
operand_2 .set('')
result    .set('')

# The top of the calculator.
top = Frame(calculator)
operand_1_input = Entry(top, textvariable=operand_1, font=FONT_1, bg='gray30', fg='white', insertbackground='white', width=5, justify='right')
operator_sign   = Label(top, textvariable=current_op, font=FONT_1, bg='gray20', fg='white')
operand_2_input = Entry(top, textvariable=operand_2, font=FONT_1, bg='gray30', fg='white', insertbackground='white', width=5, justify='right')
equal_sign      = Label(top, text='=', font=FONT_1, bg='gray20', fg='white')
result_output   = Entry(top, textvariable=result, font=FONT_1, readonlybackground='gray30', fg='white', width=6, justify='right', state='readonly')
operand_1_input.grid(column=0, row=0)
operator_sign  .grid(column=1, row=0)
operand_2_input.grid(column=2, row=0)
equal_sign     .grid(column=3, row=0)
result_output  .grid(column=4, row=0)
top.pack(pady=(15, 5))

# The fraction checkbox below the top of the calculator.
fraction_mode = BooleanVar()
fraction_mode.set(False)
fraction_toggle = Checkbutton(calculator, text='Fraction Result ', variable=fraction_mode, font=FONT_2, onvalue=True, offvalue=False, cursor='hand2', bg='gray10', fg='white', activebackground='gray10', activeforeground='yellow', selectcolor='gray10', relief=RAISED)
fraction_toggle.pack(pady=10)

# The numpad of the calculator.
numpad  = Frame(calculator)
equal   = Button(numpad, text=' = ', font=FONT_1, command=get_result, cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black')                         .grid(column=0, row=5, columnspan=3, sticky=W+E)
sign    = Button(numpad, text=' - ', font=FONT_1, command=lambda: insert_number('-'), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=10).grid(column=0, row=4)
zero    = Button(numpad, text=' 0 ', font=FONT_1, command=lambda: insert_number(0), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=6)   .grid(column=1, row=4)
decimal = Button(numpad, text=' . ', font=FONT_1, command=lambda: insert_number('.'), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=12).grid(column=2, row=4)
one     = Button(numpad, text=' 1 ', font=FONT_1, command=lambda: insert_number(1), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=5)   .grid(column=0, row=3)
two     = Button(numpad, text=' 2 ', font=FONT_1, command=lambda: insert_number(2), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=6)   .grid(column=1, row=3)
three   = Button(numpad, text=' 3 ', font=FONT_1, command=lambda: insert_number(3), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=5)   .grid(column=2, row=3)
four    = Button(numpad, text=' 4 ', font=FONT_1, command=lambda: insert_number(4), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=5)   .grid(column=0, row=2)
five    = Button(numpad, text=' 5 ', font=FONT_1, command=lambda: insert_number(5), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=6)   .grid(column=1, row=2)
six     = Button(numpad, text=' 6 ', font=FONT_1, command=lambda: insert_number(6), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=5)   .grid(column=2, row=2)
seven   = Button(numpad, text=' 7 ', font=FONT_1, command=lambda: insert_number(7), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=5)   .grid(column=0, row=1)
eight   = Button(numpad, text=' 8 ', font=FONT_1, command=lambda: insert_number(8), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=6)   .grid(column=1, row=1)
nine    = Button(numpad, text=' 9 ', font=FONT_1, command=lambda: insert_number(9), cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=5)   .grid(column=2, row=1)
clear   = Button(numpad, text='CLEAR', font=FONT_1, command=clear_entries, cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black')                    .grid(column=0, row=0, columnspan=2, sticky=W+E)
delete  = Button(numpad, text='⌫', font=FONT_1, command=delete_character, cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black', padx=0)            .grid(column=2, row=0)
numpad.pack()

# The operator selection of the calculator.
operator = IntVar()
operator.set(ADD)
operator_selection = LabelFrame(calculator, text='Operators', bg='gray10', fg='white', font=FONT_3)
divison            = Radiobutton(operator_selection, text='÷', font=FONT_2, variable=operator, value=1, command=change_operator, cursor='hand2', bg='gray10', fg='white', activebackground='gray10', activeforeground='yellow', selectcolor='gray10').grid(column=0, row=0)
multiplication     = Radiobutton(operator_selection, text='x', font=FONT_2, variable=operator, value=2, command=change_operator, cursor='hand2', bg='gray10', fg='white', activebackground='gray10', activeforeground='yellow', selectcolor='gray10').grid(column=0, row=1)
addition           = Radiobutton(operator_selection, text='+', font=FONT_2, variable=operator, value=3, command=change_operator, cursor='hand2', bg='gray10', fg='white', activebackground='gray10', activeforeground='yellow', selectcolor='gray10').grid(column=0, row=2)
subtration         = Radiobutton(operator_selection, text='-', font=FONT_2, variable=operator, value=4, command=change_operator, cursor='hand2', bg='gray10', fg='white', activebackground='gray10', activeforeground='yellow', selectcolor='gray10').grid(column=0, row=3)
operator_selection.place(x=494, y=300)

# The show history button.
open_history = Button(calculator, text='Show History', font=FONT_3, command=show_history, cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black')
open_history.place(x=11, y=360)

# The open graph button.
open_graph = Button(calculator, text='Open Graph', font=FONT_3, command=show_graph, cursor='hand2', bg='gray10', fg='white', activebackground='yellow', activeforeground='black')
open_graph.place(x=13, y=400)

# The message below the equal button indicating whether the operation has succeeded or failed.
status = StringVar()
status_message = Message(calculator, textvariable=status, bg='gray20', fg='white', font=FONT_3, width=150, justify='center')

# Event binding and protocols.
calculator.bind('<Return>', get_result)
# calculator.bind('<Return>', who_is_focused)
calculator.protocol('WM_DELETE_WINDOW', on_window_close_request)

calculator.mainloop()