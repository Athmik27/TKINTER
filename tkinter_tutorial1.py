import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("GUI PROGRAM")
window.geometry("400x300")

toolbar = tk.Frame(window)


def new_file():
    #entry.delete(0, tk.END)
    label.config(text="Enter your name:")
    #messagebox.showinfo("Clear", "Data cleared successfully")
    

def save_file():
    name = entry.get()
    messagebox.showinfo("Saved", "Data saved successfully")


def show_name():
    name = entry.get()
    print(name)


def clear_file():
    entry.delete(0, tk.END)
    messagebox.showinfo("Clear", "Data cleared successfully")

#statusbar method

status=tk.Label(
    window,
    text="Happy Program",
    anchor="center"

)
status.pack(fill="x")

# Toolbar buttons
new_button = tk.Button(toolbar, text="New", command=new_file)
save_button = tk.Button(toolbar, text="Save", command=save_file)
clear_button = tk.Button(toolbar, text="Clear",command=clear_file)


new_button.pack(side="left")
save_button.pack(side="left")
clear_button.pack(side="left")

toolbar.pack()


# Entry
entry = tk.Entry(window)
entry.pack()


# Label
label = tk.Label(
    window,
    text="Enter Your Name:",
    font=("Arial", 30),
    bg="white",
    fg="blue"
)
label.pack()


# Submit button
button = tk.Button(
    window,
    text="Submit",
    command=show_name
)
button.pack()


window.mainloop()