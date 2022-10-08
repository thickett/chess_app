import tkinter
from tkinter import ttk

root = tkinter.Tk()

frm = ttk.Frame(root,padding=10,height=255,width=255)

frm.grid()

ttk.Label(frm,text="Hello World!").grid(column=1,row=0)
ttk.Button(frm,text="quit",command=root.destroy).grid(column=1,row=2)

root.mainloop()