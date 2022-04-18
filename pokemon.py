from tkinter import *
import pyglet, tkinter
from PIL import ImageTk,Image

#Function to change screen
def homeToSelect():
    canvas.delete("all")
    selectionScreen()

def selectToBattle():
    canvas.delete("all")

#Create root screen
root = Tk()
root.title("Pokemon")
root.geometry("960x600")

#Create canvas
canvas = Canvas(root,width=960,height=600,)
canvas.pack(fill="both",expand=True)


#Creates home screen
def homeScreen():
    global bg,title
    #Open and create background image
    img = Image.open('background.png')
    img = img.resize((960,600))
    bg = ImageTk.PhotoImage(img)
    canvas.create_image(0,0,image=bg, anchor=NW)

    #Open and create title image
    title = Image.open('pokemon.png')
    title = title.resize((320,118))
    title = ImageTk.PhotoImage(title)
    canvas.create_image(320,100,anchor=NW,image=title)

    #Button for home screen
    homeButton = Button(root,text="Click to Start",command=homeToSelect)
    canvas.create_window(450,450,anchor=NW,window=homeButton)

#Creates selection screen
def selectionScreen():
    global diaBox,bg
    #Background
    canvas.configure(bg='gray')
    
    #big text box
    box = Image.open('dialog box.png')
    box = box.resize((924,422))
    diaBox = ImageTk.PhotoImage(box)
    canvas.create_image(20,125,anchor=NW,image=diaBox)

    #Dropdowns
    options = ['1','2','3']
    clicked = StringVar()
    clicked.set("Pick Your Pokemon")
    drop1 = OptionMenu(root,clicked,*options)
    canvas.create_window(100,240,anchor=NW,window=drop1)

    options = ['4','5','6']
    clicked1 = StringVar()
    clicked1.set("Pick Opponent's Pokemon")
    drop2 = OptionMenu(root,clicked1,*options)
    canvas.create_window(100,340,anchor=NW,window=drop2)
    
    #Label
    canvas.create_text(500,40,text="Pick Your Pokemon",font=("Helvetica",35))

    #Battle Button
    battleButton = Button(root,text="Battle!",command=selectToBattle)
    canvas.create_window(480,550,anchor=NW,window=battleButton)

selectionScreen()

root.mainloop()


