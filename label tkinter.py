import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("REGISTRATION FORM")
window.geometry("400x300")



def Program():
    NAME = NAME_entry.get()
    AGE = AGE_entry.get()
    print(NAME)
    print(AGE)
    print("DETAILS ADDED SUCCESSFULLY")
    messagebox.showinfo("SUCCESS","DATA ADDED SUCCESSFULLY")
def Clear():
    NAME_entry.delete(0,tk.END)
    AGE_entry.delete(0,tk.END)
    print("DETAILS CLEARED SUCCESSFULLY")
    messagebox.showinfo("SUCCESS","DATA CLEARED SUCCESSFULLY")

Label_1=tk.Label(
    window,
    text="NAME")
Label_1.grid(row=0,column=0)

NAME_entry=tk.Entry(window)
NAME_entry.grid(row=0, column=1)

Label_2=tk.Label(
    window,
    text="AGE")
Label_2.grid(row=1,column=0)

AGE_entry=tk.Entry(window)
AGE_entry.grid(row=1, column=1)

Button=tk.Button(window,text="SUBMIT",command=Program)
Button.grid(
    row=2,
    column=0,
    columnspan=2)
Button=tk.Button(window,text="CLEAR",command=Clear)
Button.grid(
    row=3,
    column=0,
    columnspan=2
)
window.mainloop()