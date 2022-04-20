from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

#Function to change screen
def homeToSelect():
    canvas.delete("all")
    selectionScreen()

def selectToBattle():
    global userPokemon,oppPokemon
    global userMove1,userMove2,userMove3,userMove4
    userPokemon = drop1.get()
    oppPokemon = drop2.get()
    canvas.delete("all")
    battleScreen()
    userMove1 = moveDrop1.get()
    userMove2 = moveDrop2.get()
    userMove3 = moveDrop3.get()
    userMove4 = moveDrop4.get()
#Function to Select Moves
def moveSelector(pokemon):
    global moves
    moves = []
    move = ""
    pokeID = 0
    print(pokemon)
    pokeFile = open("CIS-1051\pokemon.csv", "r")
    pokeFile = pokeFile.readlines()[1:152]
    for line in pokeFile:
        line = line.split(",")
        if line[1].capitalize() == pokemon:
            pokeID = line[0]
    moveFile = open("CIS-1051\pokemon_moves.csv", "r")
    moveFile = moveFile.readlines()
    with open("CIS-1051\move_names.csv", "r",errors='replace') as nameFile:
        nameFile = nameFile.readlines()
    for line in moveFile:
        line = line.split(",")
        if line[0] == pokeID and line[1] == "2":
            move = line[2]
            for row in nameFile:
                row = row.split(",")
                if move == row[0] and row[1] == "9":
                    moves.append(row[2])
    for i in range(len(moves)):
        moves[i] = moves[i][:-1]
    
def userMS(Pokemon):
    global moveDrop1,moveDrop2,moveDrop3,moveDrop4
    moveSelector(Pokemon)
    moveDrop1 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop1.set("Pick a Move")
    moveDrop2 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop2.set("Pick a Move")
    moveDrop3 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop3.set("Pick a Move")
    moveDrop4 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop4.set("Pick a Move")
    canvas.create_window(400,220,anchor=NW,window=moveDrop1)
    canvas.create_window(400,260,anchor=NW,window=moveDrop2)
    canvas.create_window(600,220,anchor=NW,window=moveDrop3)
    canvas.create_window(600,260,anchor=NW,window=moveDrop4)
    

def computerMS(Pokemon):
    global moveDrop1,moveDrop2,moveDrop3,moveDrop4
    moveSelector(Pokemon)
    moveDrop1 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop1.set("Pick a Move")
    moveDrop2 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop2.set("Pick a Move")
    moveDrop3 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop3.set("Pick a Move")
    moveDrop4 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop4.set("Pick a Move")
    canvas.create_window(400,320,anchor=NW,window=moveDrop1)
    canvas.create_window(400,360,anchor=NW,window=moveDrop2)
    canvas.create_window(600,320,anchor=NW,window=moveDrop3)
    canvas.create_window(600,360,anchor=NW,window=moveDrop4)

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
    img = Image.open('CIS-1051/background.png')
    img = img.resize((960,600))
    bg = ImageTk.PhotoImage(img)
    canvas.create_image(0,0,image=bg, anchor=NW)

    #Open and create title image
    title = Image.open("CIS-1051\pokemon.png")
    title = title.resize((320,118))
    title = ImageTk.PhotoImage(title)
    canvas.create_image(320,100,anchor=NW,image=title)

    #Button for home screen
    homeButton = Button(root,text="Click to Start",command=homeToSelect)
    canvas.create_window(450,450,anchor=NW,window=homeButton)

#Creates selection screen
def selectionScreen():
    global diaBox,bg,moves,drop1,drop2
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
    drop1.bind("<<ComboboxSelected>>",lambda _ : userMS(drop1.get()))
    canvas.create_window(100,240,anchor=NW,window=drop1)

    drop2 = ttk.Combobox(root,state="readonly",value=options)
    drop2.set("Pick Opponent's Pokemon")
    drop2.bind("<<ComboboxSelected>>",lambda _ : computerMS(drop2.get()))
    canvas.create_window(100,340,anchor=NW,window=drop2)
    
    #Label
    canvas.create_text(500,40,text="Pick Your Pokemon",font=("Helvetica",35))

    #Battle Button
    battleButton = Button(root,text="Battle!",command=selectToBattle)
    canvas.create_window(480,550,anchor=NW,window=battleButton)

#Creates battle screen
def battleScreen():
    global battleBG,cpuPokeImg,userPokeImg,borderImg,oppBorderImg
    global move1,move2,move3,move4
    #Open and create background image
    battleImg = Image.open('CIS-1051/battle background.png')
    battleImg = battleImg.resize((960,600))
    battleBG = ImageTk.PhotoImage(battleImg)
    canvas.create_image(0,0,image=battleBG, anchor=NW)

    #Creating pokemon images
    pokeID = 0
    pokeFile = open("CIS-1051\pokemon.csv","r")
    pokeFile = pokeFile.readlines()
    for line in pokeFile:
        line = line.split(",")
        if line[1].capitalize() == oppPokemon:
            pokeID = line[0]
    cpuPokeImg = PhotoImage(file="CIS-1051/ruby-sapphire/" + str(pokeID)+".png")
    cpuPokeImg = cpuPokeImg.zoom(3,3)
    canvas.create_image(600,385,anchor=SW,image=cpuPokeImg)
    for line in pokeFile:
        line = line.split(",")
        if line[1].capitalize() == userPokemon:
            pokeID = line[0]
    userPokeImg = PhotoImage(file="CIS-1051/ruby-sapphire/back/" + str(pokeID)+".png")
    userPokeImg = userPokeImg.zoom(3,3)
    canvas.create_image(200,485,anchor=SW,image=userPokeImg)

    #Battle Menu
    borderImg = PhotoImage(file="CIS-1051\moveBox.png")
    borderImg = borderImg.subsample(2,3)
    canvas.create_image(0,415,anchor=NW,image=borderImg)

    move1 = Button(root,text=userMove1,width=15,height=2)
    move2 = Button(root,text=userMove2,width=15,height=2)
    move3 = Button(root,text=userMove3,width=15,height=2)
    move4 = Button(root,text=userMove4,width=15,height=2)
    canvas.create_window(500,460,anchor=NW,window=move1)
    canvas.create_window(640,460,anchor=NW,window=move2)
    canvas.create_window(500,510,anchor=NW,window=move3)
    canvas.create_window(640,510,anchor=NW,window=move4)

    canvas.create_text(180,480,text=userPokemon,font=("Helvetica",25))

    oppBorderImg = PhotoImage(file="CIS-1051\moveBox.png")
    oppBorderImg = oppBorderImg.subsample(4,4)
    canvas.create_image(55,40,anchor=NW,image=oppBorderImg)

    canvas.create_text(170,90,text=oppPokemon,font=("Helvetica",20))

selectionScreen()

root.mainloop()