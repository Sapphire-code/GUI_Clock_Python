from tkinter import *
from tkinter.ttk import *
from time import strftime
import tkinter as tk
root = tk.Tk()

root.title("Clock")
root.geometry("500x100")
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 78), background=("black"), foreground=("cyan"))
label.pack(anchor = 'center')
time()

mainloop()
