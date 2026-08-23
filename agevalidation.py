import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.title("AGE VALIDATION FORM")
window.geometry("400x300")


def Submit():

    age = Age.get()

    if age == "":
        messagebox.showwarning("Warning", "Please fill the fields")

    elif int(age) < 18:
        messagebox.showwarning("Warning", "Age must be 18 or above")

    else:
        messagebox.showinfo(
            "Success",
            f"Age: {age}\n\nRegistration successful!"
        )


def Clear():

    Age.delete(0, tk.END)

    messagebox.showinfo(
        "Success",
        "Details Deleted Successfully"
    )


Age_label = tk.Label(window, text="Age")
Age_label.pack()

Age = tk.Entry(window)
Age.pack()


Submit_button = tk.Button(
    window,
    text="Submit",
    command=Submit
)
Submit_button.pack()


Clear_button = tk.Button(
    window,
    text="Clear",
    command=Clear
)
Clear_button.pack()


window.mainloop()