from textwrap import fill
from tkinter import *
from PIL import ImageTk,Image

#Create root screen
root = Tk()
root.title("Pokemon")
root.geometry("1000x800")

#Open background image
bg = Image.open('background.png')

background = Canvas(root)
background.pack(fill = "both")
bg = ImageTk.PhotoImage(bg)
background.create_image(100,100,image=bg)


#Open and place pokemon logo
img1= Image.open('pokemon.png')
img1 = img1.resize((2650//4,942//4))
canvas = Canvas(root,width=10000,height=10000)
canvas.pack()
img = ImageTk.PhotoImage(img1)
canvas.create_image(500,400, image=img)



root.mainloop()