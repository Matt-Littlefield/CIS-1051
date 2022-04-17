from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

#Function to change screen
def homeToSelect():
    canvas.delete("all")
    selectionScreen()

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
    canvas.create_image(320,100,anchor="nw",image=title)

    #Button for home screen
    homeButton = Button(root,text="Click to Start",command=homeToSelect)
    canvas.create_window(450,450,anchor=NW,window=homeButton)

#Creates selection screen
def selectionScreen():
    #Background
    #canvas.configure(bg='gray')

    #Dropdowns
    """
    frame = Frame(root)
    frame.pack()
    values = ['1','2','3']
    list1 = ttk.Combobox(frame,values = values)
    list1.set("Pick a Pokemon")
    list1.pack(padx=100,pady=100)
    canvas.create_window(450,450,anchor=NW,window=list1)
    """
    options = ['1','2','3']
    clicked = StringVar()
    clicked.set("Pick a Pokemon")
    drop = OptionMenu(root,clicked,*options)
    canvas.create_window(450,450,anchor=NW,window=drop)

    

selectionScreen()

root.mainloop()


