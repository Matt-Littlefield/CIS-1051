from textwrap import fill
from tkinter import *
from PIL import ImageTk,Image

#Create root screen
root = Tk()
root.title("Pokemon")
root.geometry("1920x1200")
root.config(bg="blue")

#Open background image
"""
bg = Image.open('background.png')
bg = bg.resize((1920,1200))
background = ImageTk.PhotoImage(bg)
label1 = Label(root, image = background)
label1.pack(expand=True,fill='both')
"""
#Open and place pokemon logo
img1= Image.open('pokemon.png')
img1 = img1.resize((2650//10,942//10))
canvas = Canvas(root,width=10000,height=10000)
canvas.pack()
img = ImageTk.PhotoImage(img1)
canvas.create_image(500,400, image=img)



root.mainloop()