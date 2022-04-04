from tkinter import *

root = Tk()

root.title("Welcome")

root.geometry("300x300")

lbl = Label(root, text = "Hello There :)")
lbl.grid()

def clicked():
    lbl.configure(text = "CLICK")

btn = Button(root, text = "Click the button", fg="red", command = clicked)
btn.grid(column=1,row=0)

root.mainloop()