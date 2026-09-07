 What is Tkinter?

**Tkinter** is Python's built-in library for creating **GUI (Graphical User Interface)** applications.

GUI means applications that have:

* Windows
* Buttons
* Labels
* Text boxes
* Menus
* Checkboxes
* Input fields

Examples of GUI applications:

* Calculator
* Login Form
* Registration Form
* To-Do List
* Simple Games
* Student Management System

---


Tkinter usually comes with Python, so you normally don't need to install it separately.



A commonly used import is:

```python
import tkinter as tk
```

---

# 🪟 Creating a Window

The first step in a Tkinter application is creating the main window.

### Syntax

```python
import tkinter as tk

root = tk.Tk()

root.mainloop()
```

### Explanation

* `tk.Tk()` → creates the main window
* `root` → variable containing the window
* `mainloop()` → keeps the window running

---

# 🏷️ Label

A **Label** is used to display text.

```python
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello World")

label.pack()

root.mainloop()
```

### Important

```python
tk.Label(root, text="Hello World")
```

* `root` → parent window
* `text` → text displayed on the label

---

# 🔘 Button

A **Button** allows the user to perform an action.

```python
import tkinter as tk

root = tk.Tk()

def hello():
    print("Hello!")

button = tk.Button(root, text="Click Me", command=hello)

button.pack()

root.mainloop()
```

### `command`

```python
command=hello
```

This tells Tkinter:

> Run the `hello()` function when the button is clicked.

### ⚠️ Common mistake

Don't write:

```python
command=hello()
```

Use:

```python
command=hello
```

---

# 📝 Entry

An **Entry** is used to take input from the user.

```python
import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)

entry.pack()

root.mainloop()
```

### Getting the entered value

```python
name = entry.get()

print(name)
```

---

# 📦 Frame

A **Frame** is a container used to organize widgets.

```python
frame = tk.Frame(root)

frame.pack()
```

You can place widgets inside the frame:

```python
label = tk.Label(frame, text="Hello")

label.pack()
```

---

# 📐 Geometry Managers

Tkinter provides three main ways to position widgets.

## 1. `pack()`

Simple and commonly used.

```python
label.pack()
```

You can specify a direction:

```python
label.pack(side="left")
```

---

## 2. `grid()`

Places widgets in rows and columns.

```python
label.grid(row=0, column=0)

entry.grid(row=0, column=1)
```

Example:

```text
        Column 0       Column 1

Row 0   Name:          [       ]

Row 1   Age:           [       ]
```

---

## 3. `place()`

Places widgets using exact coordinates.

```python
label.place(x=50, y=100)
```

### ⚠️ Important

Avoid mixing `pack()` and `grid()` inside the **same parent/container**.

---

# 🎨 Changing Widget Appearance

You can change the appearance of widgets.

```python
label = tk.Label(
    root,
    text="Hello",
    bg="blue",
    fg="white",
    font=("Arial", 20)
)

label.pack()
```

Common options:

| Option   | Meaning             |
| -------- | ------------------- |
| `text`   | Text displayed      |
| `bg`     | Background color    |
| `fg`     | Text color          |
| `font`   | Font style and size |
| `width`  | Width               |
| `height` | Height              |
| `padx`   | Horizontal padding  |
| `pady`   | Vertical padding    |

---

# 🖱️ Button Example

```python
button = tk.Button(
    root,
    text="Click Me",
    bg="green",
    fg="white",
    font=("Arial", 15)
)

button.pack()
```

---

# 🔢 Simple Calculator Example

```python
import tkinter as tk

root = tk.Tk()

root.title("Calculator")

entry = tk.Entry(root)

entry.pack()


def add():
    num1 = int(entry.get())
    print(num1 + 10)


button = tk.Button(
    root,
    text="Add 10",
    command=add
)

button.pack()

root.mainloop()
```

---

# 💬 Message Box

Tkinter provides message boxes for displaying messages.

```python
from tkinter import messagebox
```

Example:

```python
messagebox.showinfo("Message", "Hello!")
```

Other useful message boxes:

```python
messagebox.showinfo()
messagebox.showwarning()
messagebox.showerror()
messagebox.askyesno()
```

Example:

```python
from tkinter import messagebox

messagebox.showerror(
    "Error",
    "Something went wrong!"
)
```

---

# 📝 Text Widget

`Text` is used when you need a larger text area.

```python
text = tk.Text(root)

text.pack()
```

Getting text:

```python
data = text.get("1.0", tk.END)

print(data)
```

---

# ☑️ Checkbutton

Used for selecting or unselecting an option.

```python
check = tk.Checkbutton(
    root,
    text="I agree"
)

check.pack()
```

---

# 🔘 Radiobutton

Used when the user should select **one option** from multiple choices.

```python
choice = tk.StringVar()

radio1 = tk.Radiobutton(
    root,
    text="Male",
    variable=choice,
    value="Male"
)

radio2 = tk.Radiobutton(
    root,
    text="Female",
    variable=choice,
    value="Female"
)

radio1.pack()
radio2.pack()
```

Get the selected value:

```python
print(choice.get())
```

---

# 📋 Listbox

Used to display a list of items.

```python
listbox = tk.Listbox(root)

listbox.pack()

listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C")
```

---

# 🏷️ Window Title

Change the window title:

```python
root.title("My Application")
```

---

# 📏 Window Size

Set the window size:

```python
root.geometry("500x400")
```

Format:

```text
width x height
```

Example:

```python
root.geometry("800x600")
```

---

# ❌ Closing the Window

You can close the application using:

```python
root.destroy()
```

Example:

```python
def close_window():
    root.destroy()
```

---

# 🔄 Tkinter Program Structure

A basic Tkinter application generally follows this structure:

```python
import tkinter as tk

# Create window
root = tk.Tk()

# Create widgets
label = tk.Label(root, text="Hello")
button = tk.Button(root, text="Click")

# Position widgets
label.pack()
button.pack()

# Run application
root.mainloop()
```

Remember this flow:

```text
Import Tkinter
      ↓
Create Window
      ↓
Create Widgets
      ↓
Position Widgets
      ↓
Add Functions
      ↓
mainloop()
```

---

# 🧠 Important Tkinter Widgets

| Widget        | Purpose                 |
| ------------- | ----------------------- |
| `Tk()`        | Creates main window     |
| `Label`       | Displays text           |
| `Button`      | Performs an action      |
| `Entry`       | Takes single-line input |
| `Text`        | Takes multi-line input  |
| `Frame`       | Organizes widgets       |
| `Checkbutton` | Checkbox                |
| `Radiobutton` | Select one option       |
| `Listbox`     | Displays a list         |
| `Scale`       | Slider                  |
| `Spinbox`     | Select a value          |

---

# 🔥 Mini Login Form

```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Login")
root.geometry("300x200")


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")


tk.Label(root, text="Username").pack()

username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(
    root,
    text="Login",
    command=login
).pack()

root.mainloop()
```

---

# ⚠️ Common Mistakes

### 1. Forgetting `mainloop()`

Wrong:

```python
root = tk.Tk()
```

Correct:

```python
root = tk.Tk()
root.mainloop()
```

---

### 2. Calling the function immediately

Wrong:

```python
command=login()
```

Correct:

```python
command=login
```

---

### 3. Forgetting to position widgets

Creating a widget is not enough.

```python
label = tk.Label(root, text="Hello")
```

You also need:

```python
label.pack()
```

or:

```python
label.grid(row=0, column=0)
```




# Quick Cheat Sheet

```python
import tkinter as tk
from tkinter import messagebox

# Window
root = tk.Tk()

root.title("My App")
root.geometry("500x400")

# Label
label = tk.Label(root, text="Hello")

# Button
button = tk.Button(root, text="Click")

# Entry
entry = tk.Entry(root)

# Text
text = tk.Text(root)

# Frame
frame = tk.Frame(root)

# Position
label.pack()
button.pack()
entry.pack()

# Get Entry value
value = entry.get()

# Message box
messagebox.showinfo("Title", "Message")

# Run
root.mainloop()
```

---

# 📚 Key Points to Remember

* **Tkinter = Python GUI library**
* `Tk()` creates the main window.
* `Label` displays text.
* `Button` performs an action.
* `Entry` takes user input.
* `Frame` organizes widgets.
* `pack()`, `grid()`, and `place()` position widgets.
* `command` connects a button to a function.
* `mainloop()` keeps the application running.
* `messagebox` displays popup messages.
* `get()` retrieves user input.

---


