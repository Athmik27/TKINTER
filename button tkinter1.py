import tkinter as tk

window=tk.Tk()
window.title("MY GUI PROGRAM")
window.geometry("400x300")

def Hello():
    print("BUTTON_1 CLICKED ")

def Hi():
    print("BUTTON_2 CLICKED ")

def Hey():
    print("BUTTON_3 CLICKED ")


Button1=tk.Button(window,text="CLICK ME",command=Hello)
Button1.pack(side="left")

Button2=tk.Button(window,text="CLICK ME",command=Hi)
Button2.pack(side="right")

Button3=tk.Button(window,text="CLICK ME",command=Hey)
Button3.pack(side="bottom")

window.mainloop()

#######
import tkinter as tk

window=tk.Tk()
window.title("My Gui Program")
window.geometry("400x300")

def Hello():
    print("BUTTON_1 CLICKED ")

Button_1=tk.Button(window,text="BUTTON_1",command=Hello)
Button_1.pack(fill="x")
window.mainloop()
##########
import tkinter as tk

window=tk.Tk()
window.title("My Gui Program")
window.geometry("400x300")

def Hello():
    print("BUTTON_1 CLICKED ")

def Hi():
    print("BUTTON_2 CLICKED ")

def Hey():
   print("BUTTON_3 CLICKED ")

Button_1=tk.Button(window,text="CLICK_ME",command=Hello)
Button_1.pack(padx="10",pady="10")

Button_2=tk.Button(window,text="BUTTON_2",command=Hi)
Button_2.pack(fill="x")

Button_3=tk.Button(window,text="BUTTON_3",command=Hey)
Button_3.pack(fill="x")



window.mainloop()