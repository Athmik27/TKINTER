
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.title("REGISTRATION FORM")
window.geometry("400x350")


def submit():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()

    if name == "" or age == "" or email == "":
        messagebox.showwarning("Warning", "Please fill all fields")

    else:
        messagebox.showinfo(
            "Success",
            f"Name: {name}\nAge: {age}\nEmail: {email}\n\nRegistration successful!"
        )


def clear():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    messagebox.showinfo("Clear", "Data cleared successfully")


# Name
name_label = tk.Label(window, text="Name")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()


# Age
age_label = tk.Label(window, text="Age")
age_label.pack()

age_entry = tk.Entry(window)
age_entry.pack()

# Email
email_label = tk.Label(window, text="Email")
email_label.pack()

email_entry = tk.Entry(window)
email_entry.pack()


# Submit button
submit_button = tk.Button(
    window,
    text="Submit",
    command=submit
)
submit_button.pack()

# Clear button
clear_button = tk.Button(
    window,
    text="Clear",
    command=clear
)
clear_button.pack()


window.mainloop()