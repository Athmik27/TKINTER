#  Tkinters

Tkinter is Python's **standard GUI library** used to create desktop applications with graphical user interfaces.

GUI means **Graphical User Interface**.

```python
import tkinter as tk
```

---

## 1. Create Main Window

```python
import tkinter as tk

root = tk.Tk()

root.mainloop()
```

### Important

```text
tk.Tk()       → Creates the main window
mainloop()    → Keeps the window running
```

---

## 2. Window Title

```python
root.title("My Application")
```

---

## 3. Window Size

```python
root.geometry("500x400")
```

Format:

```text
width x height
```

Example:

```text
500x400
```

---

## 4. Window Background

```python
root.configure(
    bg="lightblue"
)
```

---

## 5. Label

A Label is used to **display text or information**.

```python
label = tk.Label(
    root,
    text="Hello World"
)

label.pack()
```

---

## 6. Button

A Button is used to **perform an action when clicked**.

```python
def hello():
    print("Button clicked")

button = tk.Button(
    root,
    text="Click Me",
    command=hello
)

button.pack()
```

### `command`

```python
command=hello
```

Connects the button to a function.

Do not use:

```python
command=hello()
```

because that calls the function immediately.

---

## 7. Entry

Entry is used to **take input from the user**.

```python
entry = tk.Entry(root)

entry.pack()
```

Get the entered value:

```python
value = entry.get()

print(value)
```

---

## 8. Text

Text widget is used for **multi-line text input**.

```python
text = tk.Text(
    root,
    height=5,
    width=30
)

text.pack()
```

Get text:

```python
value = text.get(
    "1.0",
    tk.END
)
```

---

## 9. Checkbutton

Used when the user can select or deselect an option.

```python
check_var = tk.BooleanVar()

check = tk.Checkbutton(
    root,
    text="I Agree",
    variable=check_var
)

check.pack()
```

Get the value:

```python
print(check_var.get())
```

---

## 10. Radio Button

Used when the user must select **one option from multiple choices**.

```python
gender = tk.StringVar()

tk.Radiobutton(
    root,
    text="Male",
    variable=gender,
    value="Male"
).pack()

tk.Radiobutton(
    root,
    text="Female",
    variable=gender,
    value="Female"
).pack()
```

Get selected value:

```python
print(gender.get())
```

---

## 11. Listbox

Used to display a **list of selectable items**.

```python
listbox = tk.Listbox(root)

listbox.insert(
    tk.END,
    "Python"
)

listbox.insert(
    tk.END,
    "Java"
)

listbox.pack()
```

Get selected item:

```python
selected = listbox.get(
    listbox.curselection()
)

print(selected)
```

---

## 12. Frame

A Frame is used to **group widgets together**.

```python
frame = tk.Frame(
    root,
    bg="lightblue"
)

frame.pack()
```

Example:

```python
label = tk.Label(
    frame,
    text="Hello"
)

label.pack()
```

---

## 13. Message

Used to display **multi-line text**.

```python
message = tk.Message(
    root,
    text="Welcome to Tkinter"
)

message.pack()
```

---

## 14. Messagebox

Used to display popup messages.

```python
from tkinter import messagebox
```

Information:

```python
messagebox.showinfo(
    "Information",
    "Operation successful"
)
```

Warning:

```python
messagebox.showwarning(
    "Warning",
    "Check your input"
)
```

Error:

```python
messagebox.showerror(
    "Error",
    "Something went wrong"
)
```

Question:

```python
messagebox.askyesno(
    "Question",
    "Do you want to continue?"
)
```

---

## 15. Geometry Managers

Tkinter provides three main geometry managers:

```text
pack()
grid()
place()
```

---

## 16. `pack()`

Arranges widgets automatically.

```python
label.pack()
```

With options:

```python
label.pack(
    padx=20,
    pady=10
)
```

---

## 17. `grid()`

Arranges widgets in **rows and columns**.

```python
label.grid(
    row=0,
    column=0
)

entry.grid(
    row=0,
    column=1
)
```

Example:

```python
tk.Label(
    root,
    text="Name"
).grid(row=0, column=0)

tk.Entry(
    root
).grid(row=0, column=1)
```

---

## 18. `place()`

Positions widgets using exact coordinates.

```python
button.place(
    x=100,
    y=150
)
```

---

## 19. Important Geometry Parameters

### `padx`

Adds horizontal space.

```python
button.pack(
    padx=20
)
```

### `pady`

Adds vertical space.

```python
button.pack(
    pady=20
)
```

### `ipadx`

Adds internal horizontal space.

### `ipady`

Adds internal vertical space.

---

## 20. Widget Properties

Common properties:

```python
button = tk.Button(
    root,
    text="Click",
    bg="blue",
    fg="white",
    font=("Arial", 14),
    width=15,
    height=2
)
```

Common options:

```text
text
bg
fg
font
width
height
state
anchor
padx
pady
```

---

## 21. Disable Button

```python
button = tk.Button(
    root,
    text="Disabled",
    state="disabled"
)
```

Enable later:

```python
button.config(
    state="normal"
)
```

---

## 22. Change Widget Properties

Use `config()`:

```python
label.config(
    text="New Text"
)
```

Example:

```python
button.config(
    text="Updated"
)
```

---

## 23. Destroy Widget

Remove a widget:

```python
button.destroy()
```

Close the main window:

```python
root.destroy()
```

---

## 24. Tkinter Variables

Tkinter provides special variable classes:

```text
StringVar()
IntVar()
DoubleVar()
BooleanVar()
```

Example:

```python
name = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=name
)

entry.pack()
```

Get value:

```python
print(name.get())
```

Set value:

```python
name.set("Athmik")
```

---

## 25. Event Handling

Tkinter can respond to events such as:

* Mouse click
* Keyboard press
* Mouse movement

Example:

```python
def clicked(event):
    print("Mouse clicked")

root.bind(
    "<Button-1>",
    clicked
)
```

---

## 26. Keyboard Event

```python
def key_pressed(event):
    print(event.keysym)

root.bind(
    "<Key>",
    key_pressed
)
```

---

## 27. Common Events

```text
<Button-1>   → Left mouse click
<Button-2>   → Middle mouse click
<Button-3>   → Right mouse click
<Key>        → Keyboard key
<Return>     → Enter key
<Motion>     → Mouse movement
```

---

## 28. Simple Login GUI

```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Login")
root.geometry("400x300")

tk.Label(
    root,
    text="Username"
).pack()

username = tk.Entry(root)
username.pack()

tk.Label(
    root,
    text="Password"
).pack()

password = tk.Entry(
    root,
    show="*"
)

password.pack()


def login():
    user = username.get()
    pwd = password.get()

    if user == "admin" and pwd == "1234":
        messagebox.showinfo(
            "Login",
            "Login Successful"
        )
    else:
        messagebox.showerror(
            "Login",
            "Invalid Login"
        )


tk.Button(
    root,
    text="Login",
    command=login
).pack()

root.mainloop()
```

---

## 29. Important Tkinter Widgets

| Widget        | Use                     |
| ------------- | ----------------------- |
| `Tk()`        | Main window             |
| `Label`       | Display text            |
| `Button`      | Perform action          |
| `Entry`       | Single-line input       |
| `Text`        | Multi-line input        |
| `Checkbutton` | Select/deselect option  |
| `Radiobutton` | Select one option       |
| `Listbox`     | Display selectable list |
| `Frame`       | Group widgets           |
| `Message`     | Display multi-line text |
| `Menu`        | Create menus            |

---

## 30. Important Tkinter Functions

| Function      | Use                     |
| ------------- | ----------------------- |
| `Tk()`        | Create main window      |
| `mainloop()`  | Run GUI event loop      |
| `title()`     | Set window title        |
| `geometry()`  | Set window size         |
| `configure()` | Configure widget/window |
| `pack()`      | Arrange widget          |
| `grid()`      | Arrange in rows/columns |
| `place()`     | Position widget         |
| `get()`       | Get value               |
| `set()`       | Set value               |
| `config()`    | Modify widget           |
| `destroy()`   | Remove widget           |
| `bind()`      | Handle events           |

---

#  CHEAT SHEET

```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("My App")
root.geometry("500x400")

label = tk.Label(
    root,
    text="Hello"
)
label.pack()

entry = tk.Entry(root)
entry.pack()

def click():
    value = entry.get()
    print(value)

button = tk.Button(
    root,
    text="Click",
    command=click
)
button.pack()

messagebox.showinfo(
    "Info",
    "Hello"
)

root.mainloop()
```

