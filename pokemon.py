from shutil import move
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

#Function to change screen
def homeToSelect():
    canvas.delete("all")
    selectionScreen()

def selectToBattle():
    canvas.delete("all")

#Function to Select Moves
def moveSelector(pokemon):
    moveIDs = []
    moves = []
    move = ""
    pokeID = 0
    print(pokemon)
    pokeFile = open("CIS-1051\pokemon.csv", "r")
    pokeFile = pokeFile.readlines()[1:152]
    for line in pokeFile:
        line = line.split(",")
        if line[1].capitalize() == pokemon:
            print(":)")
            pokeID = line[0]
    moveFile = open("CIS-1051\pokemon_moves.csv", "r")
    moveFile = moveFile.readlines()
    nameFile = open("CIS-1051\move_names.csv", "r")
    nameFile = nameFile.readlines()
    for line in moveFile:
        line = line.split(",")
        if line[0] == pokeID and line[1] == "2":
            move = line[2]
            for row in moveFile:
                row = row.split(",")
                if move == row[0] and row[2] == "9":
                    moves.append(row[2])
    print(moves)

    
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
    box = Image.open('CIS-1051\dialog box.png')
    box = box.resize((924,422))
    diaBox = ImageTk.PhotoImage(box)
    canvas.create_image(20,125,anchor=NW,image=diaBox)

    #Dropdowns
    options = []
    pokeFile = open("CIS-1051\pokemon.csv", "r")
    pokeFile = pokeFile.readlines()[1:152]
    for line in pokeFile:
        line = line.split(",")
        options.append(line[1].capitalize())

    drop1 = ttk.Combobox(root,state="readonly",value=options)
    drop1.set("Pick Your Pokemon")
    drop1.bind("<<ComboboxSelected>>",lambda _ : moveSelector(drop1.get()))
    canvas.create_window(100,240,anchor=NW,window=drop1)

    drop2 = ttk.Combobox(root,state="readonly",value=options)
    drop2.set("Pick Opponent's Pokemon")
    canvas.create_window(100,340,anchor=NW,window=drop2)
    

    #Label
    canvas.create_text(500,40,text="Pick Your Pokemon",font=("Helvetica",35))

    #Battle Button
    battleButton = Button(root,text="Battle!",command=selectToBattle)
    canvas.create_window(480,550,anchor=NW,window=battleButton)

selectionScreen()

root.mainloop()


