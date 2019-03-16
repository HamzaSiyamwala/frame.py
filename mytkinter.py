#!/usr/bin/python

import tkinter as tk
root = tk.Tk()
logo = tk.PhotoImage(file = "python.gif" )
# w1 = tk.Label(root,image = logo).pack (side = "right")
explaination = "hi This is wat Tkinter can DO"
w = tk.Label(root,justify=tk.LEFT,compound=tk.LEFT,padx=10,text = explaination,image=logo).pack (side = "right")
root.mainloop()