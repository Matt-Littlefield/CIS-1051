from tkinter import *
from PIL import ImageTk,Image


#Create root screen
root = Tk()
root.title("Test")
root.geometry("960x600")

#Create canvas
canvas = Canvas(root,width=960,height=600,)
canvas.pack(fill="both",expand=True)

#Open and create background image
img = Image.open('background.png')
img = img.resize((960,600))
bg = ImageTk.PhotoImage(img)
canvas.create_image(0,0,image=bg, anchor=NW)

#Open and create title image
title = Image.open('pokemon.png')
title = title.resize((320,118))
title = ImageTk.PhotoImage(title)
title_window = canvas.create_image(320,100,anchor="nw",image=title)

#Button for home screen
homeButton = Button(root,text="Click to Start")
canvas.create_window(450,450,anchor=NW,window=homeButton)


root.mainloop()

f
