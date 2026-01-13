'''
@ author :      Swati Kumbhar
@ goal   :      To create a calculator which will calculate the Simple interest using tkinter
@ date   :      01/12/2026

'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys


default_msg = "The output will be displayed here"

def do_compute():
    try:
        principal = int(principal_str_var.get())
        rate = int(rate_str_var.get())
        time = int(time_str_var.get())

        if principal <= 0 or rate <= 0 or time <= 0:
            raise ValueError("Principal, rate and time must be positive real numbers")
        SI = (principal * rate * time) // 100
        total_amt = principal + SI
        output_msg = "Simple Interest:{}".format(SI)
        output_msg2 = "Total Amount:{}".format(total_amt)
        output_str_var.set(output_msg)
        output_str_var2.set(output_msg2)
    except:
        exc_name, exc_data, exc_tb = sys.exc_info()
        error_msg = "Error Type:{}. Error Message:{}. Try again". format(exc_name.__name__,str(exc_data))
        messagebox.askquestion("Error", error_msg)


def do_clear():
    empty_str = ''
    principal_str_var.set(empty_str)
    rate_str_var.set(empty_str)
    time_str_var.set(empty_str)
    output_str_var.set(default_msg)


def main():
    global principal_str_var, rate_str_var, time_str_var, output_str_var, output_str_var2, default_msg

    root_window = Tk()
    root_window.title("Simple Interest Calculator")

    input_frame = ttk.Frame(root_window, padding = "3 3 12 12", borderwidth = 10, relief = 'raised')
    input_frame.grid(column = 1, row = 1, sticky = (N, W, E, S))
    input_frame.rowconfigure(1, weight = 1)
    input_frame.columnconfigure(1, weight = 1)

    principal_msg = ttk.Label(input_frame)
    principal_msg.configure(text = "Principal (P)")
    principal_msg.grid(column = 1, row = 1, sticky = (W, E))

    rate_msg = ttk.Label(input_frame)
    rate_msg.configure(text = "Rate (R)")
    rate_msg.grid(column = 1, row = 2, sticky = (W, E))

    time_msg = ttk.Label(input_frame)
    time_msg.configure(text = "Time (T)")
    time_msg.grid(column = 1, row = 3, sticky = (W, E))

    principal_str_var = StringVar()
    principal_entry = ttk.Entry(input_frame)
    principal_entry.configure(textvariable = principal_str_var)
    principal_entry.grid(column = 2, row = 1, sticky = (W, E))

    rate_str_var = StringVar()
    rate_entry = ttk.Entry(input_frame)
    rate_entry.configure(textvariable = rate_str_var)
    rate_entry.grid(column = 2, row = 2, sticky = (W,E))

    time_str_var = StringVar()
    time_entry = ttk.Entry(input_frame)
    time_entry.configure(textvariable = time_str_var)
    time_entry.grid(column = 2, row = 3, sticky = (W, E))

    button_frame = ttk.Frame(root_window, padding = "3 3 12 12", borderwidth = 10, relief = 'raised')
    button_frame.grid(column = 1, row = 2, sticky = (N, W, E, S))
    button_frame.rowconfigure(2, weight = 1)
    button_frame.columnconfigure(1, weight = 1)

    compute_button = ttk.Button(button_frame)
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
    output_frame.rowconfigure(3, weight=1)
    output_frame.columnconfigure(1, weight = 1)

    output_str_var = StringVar()
    output_msg = ttk.Label(output_frame)
    output_msg.configure(textvariable = output_str_var)
    output_msg.grid(column = 1, row = 1, sticky = (W, E))
    output_str_var.set(default_msg)

    output_str_var2 = StringVar()
    output_msg2 = ttk.Label(output_frame)
    output_msg2.configure(textvariable = output_str_var2)
    output_msg2.grid(column = 1, row = 2, sticky = (W, E))

    for frames in root_window.winfo_children():
        frames.grid_configure(padx= 3, pady = 1)
        for widget in frames.winfo_children():
            widget.grid_configure(padx = 5, pady = 5)

    root_window.mainloop()

main()



    


