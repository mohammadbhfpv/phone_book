import tkinter as tk
from tkinter.constants import RAISED
from tkinter import messagebox
window=tk.Tk()



for i in range(3):
    for j in range(3):
        frame=tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
        frame.grid(row=i,column=j)
        Label=tk.Label(master=frame,text=f"Row{i}\nColumn{j}")
        Label.pack()
        
messagebox.showinfo(window, message="Hello!")

window.mainloop()