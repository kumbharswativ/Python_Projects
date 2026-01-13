'''
@ author : Swati Kumbhar
@ goal   : To calculate the area and the perimeter of the rectangle
@ date   : 01/12/2026
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

default_msg = "The output will be displayed here"

def do_compute():
    try:
        length = float(length_str_var.get())
        breadth = float(breadth_str_var.get())

        if length <= 0 or breadth <= 0:
            raise ValueError("Length and Breadth must be positive real numbers")
        a = length * breadth
        p = 2 * (length + breadth)
        d = ((length ** 2) + (breadth ** 2)) ** 0.5
        output_msg1 = "Area : {}". format(a)
        output_msg2 = "Perimeter : {}". format(p)
        output_msg3 = "Diagonal : {}".format(d)
        output_str_var1.set(output_msg1)
        output_str_var2.set(output_msg2)
        output_str_var3.set(output_msg3)

    except:
        exc_name, exc_data, exc_tb = sys.exc_info()
        error_msg = "Error Type: {}. Error Message: {}. Try again". format(exc_name.__name__, str(exc_data))
        messagebox.askquestion("Error", error_msg)



def do_clear():
    empty_str = ""
    length_str_var.set(empty_str)
    breadth_str_var.set(empty_str)
    output_str_var1.set(default_msg)
    output_str_var2.set(empty_str)
    output_str_var3.set(empty_str)


def main():
    global length_str_var, breadth_str_var, output_str_var1, output_str_var2, output_str_var3 ,default_msg

    root_window = Tk()
    root_window.title("Area and Perimeter of the Rectangle")

    input_frame = ttk.Frame(root_window, padding = "3 3 12 12", borderwidth = 10, relief = 'raised')
    input_frame.grid(row = 1, column = 1, sticky=(N, W, E, S))
    input_frame.rowconfigure(1, weight = 1)
    input_frame.columnconfigure(1, weight = 1)

    
    length_msg = ttk.Label(input_frame)
    length_msg.configure(text = "Enter Length")
    length_msg.grid(row = 1, column = 1, sticky = (W, E))

    breadth_msg = ttk.Label(input_frame)
    breadth_msg.configure(text = "Enter Breadth")
    breadth_msg.grid(row = 2, column = 1, sticky = (W, E))

    length_str_var = StringVar()
    length_entry = ttk.Entry(input_frame)
    length_entry.configure(textvariable = length_str_var)
    length_entry.grid(row = 1, column = 2, sticky = (W, E))

    breadth_str_var = StringVar()
    breadth_entry = ttk.Entry(input_frame)
    breadth_entry.configure(textvariable = breadth_str_var)
    breadth_entry.grid(row = 2, column = 2, sticky = (W, E))

    button_frame = ttk.Frame(root_window, padding = "3 3 12 12", borderwidth = 10, relief = "raised")
    button_frame.grid(row = 2, column = 1, sticky = (N, W, E, S))
    button_frame.rowconfigure(2, weight = 1)
    button_frame.columnconfigure(1, weight = 1)

    compute_button =  ttk.Button(button_frame)
    compute_button.configure(text = "Compute", command = do_compute)
    compute_button.grid(row = 1, column = 1, sticky = (W, E))

    clear_button = ttk.Button(button_frame)
    clear_button.configure(text = "Clear", command = do_clear)
    clear_button.grid(row = 1, column = 2, sticky = (W, E))

    exit_button = ttk.Button(button_frame)
    exit_button.configure(text = "Exit", command = sys.exit)
    exit_button.grid(row = 1, column = 3, sticky = (W, E))

    output_frame = ttk.Frame(root_window, padding = "3 3 12 12", borderwidth = 10, relief = "sunken")
    output_frame.grid(row = 3, column = 1, sticky = (N, W, E, S))
    output_frame.rowconfigure(3, weight = 1)
    output_frame.columnconfigure(1, weight = 1)

    output_str_var1 = StringVar()
    output_msg1 = ttk.Label(output_frame)
    output_msg1.configure(textvariable = output_str_var1)
    output_msg1.grid(row = 1, column = 1, sticky = (W, E))
    output_str_var1.set(default_msg)

    output_str_var2 = StringVar()
    output_msg2 = ttk.Label(output_frame)
    output_msg2.configure(textvariable = output_str_var2)
    output_msg2.grid(row = 2, column = 1, sticky = (W, E))

    output_str_var3 = StringVar()
    output_msg3 = ttk.Label(output_frame)
    output_msg3.configure(textvariable = output_str_var3)
    output_msg3.grid(row = 3, column = 1, sticky = (W, E))


    for frames in root_window.winfo_children():
        frames.grid_configure(padx = 3, pady = 1)
        for widget in frames.winfo_children():
            widget.grid_configure(padx = 5, pady = 5)

    root_window.mainloop()

main()    
