from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('450x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command = clicked)

btn.grid(column=1, row=0)

txt = Entry(window, width =10)
txt.grid(column =2, row=0)

def clicked():
    lbl.text = "Button clicked"



window.mainloop()