import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.title("STUDENT REGISTRATION")
window.geometry("400x300")


def Submit():

    name = name_entry.get()

    skills = []

    if python.get() == 1:
        skills.append("Python")

    if java.get() == 1:
        skills.append("Java")

    if kotlin.get() == 1:
        skills.append("Kotlin")

    if name == "":
        messagebox.showwarning(
            "Warning",
            "Please enter your name"
        )

    elif len(skills) == 0:
        messagebox.showwarning(
            "Warning",
            "Please select at least one skill"
        )

    else:
        messagebox.showinfo(
            "Success",
            f"Name: {name}\nSkills: {', '.join(skills)}\n\nRegistration successful!"
        )


name_label = tk.Label(window, text="NAME")
name_label.grid(row=1, column=2)

name_entry = tk.Entry(window)
name_entry.grid(row=2, column=2)


skill_label = tk.Label(window, text="SELECT SKILLS")
skill_label.grid(row=3, column=2)


python = tk.IntVar()

python_checkbutton = tk.Checkbutton(
    window,
    text="Python",
    variable=python
)

python_checkbutton.grid(row=4, column=1)


java = tk.IntVar()

java_checkbutton = tk.Checkbutton(
    window,
    text="Java",
    variable=java
)

java_checkbutton.grid(row=5, column=1)


kotlin = tk.IntVar()

kotlin_checkbutton = tk.Checkbutton(
    window,
    text="Kotlin",
    variable=kotlin
)

kotlin_checkbutton.grid(row=6, column=1)


button = tk.Button(
    window,
    text="SUBMIT",
    command=Submit
)

button.grid(row=7, column=2)


window.mainloop()