from tkinter import *
from tkinter import ttk

root = Tk() 
root.title("My first Python GUI!")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="My first Python GUI").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
root.iconbitmap("icon.ico")

root.mainloop()