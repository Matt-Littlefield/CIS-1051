from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import random

#Function to change screen
def homeToSelect():
    canvas.delete("all")
    selectionScreen()

def selectToBattle():
    global userPokemon,oppPokemon
    global userMove1,userMove2,userMove3,userMove4,oppMoves
    global checkUser,checkOpp
    userPokemon = drop1.get()
    oppPokemon = drop2.get()
    userMove1 = moveDrop1.get()
    userMove2 = moveDrop2.get()
    userMove3 = moveDrop3.get()
    userMove4 = moveDrop4.get()
    oppMoves = [moveDrop5.get(),moveDrop6.get(),moveDrop7.get(),moveDrop8.get()]
    canvas.delete("all")
    checkUser = True
    checkOpp = True
    battleScreen()

#Function to Select Moves
def moveSelector(pokemon):
    global moves
    moves = []
    move = ""
    pokeID = 0
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
        if line[0] == pokeID and line[1] == "2" and line[3] == "1":
            move = line[2]
            for row in nameFile:
                row = row.replace(" ","-")
                row = row.split(",")
                if move == row[0] and row[1] == "9" and row[2] not in moves:
                    moves.append(row[2])
    for i in range(len(moves)):
        moves[i] = moves[i][:-1]
    #moves = ["Ember","Growl","Scratch"]
    
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
    global moveDrop5,moveDrop6,moveDrop7,moveDrop8
    moveSelector(Pokemon)
    moveDrop5 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop5.set("Pick a Move")
    moveDrop6 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop6.set("Pick a Move")
    moveDrop7 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop7.set("Pick a Move")
    moveDrop8 = ttk.Combobox(root,state="readonly",value=moves)
    moveDrop8.set("Pick a Move")
    canvas.create_window(400,320,anchor=NW,window=moveDrop5)
    canvas.create_window(400,360,anchor=NW,window=moveDrop6)
    canvas.create_window(600,320,anchor=NW,window=moveDrop7)
    canvas.create_window(600,360,anchor=NW,window=moveDrop8)

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
    global pokeOptions
    #Background
    canvas.configure(bg='gray')
    
    #big text box
    box = Image.open('CIS-1051\dialog box.png')
    box = box.resize((924,422))
    diaBox = ImageTk.PhotoImage(box)
    canvas.create_image(20,125,anchor=NW,image=diaBox)

    #Dropdowns
    pokeOptions = []
    pokeFile = open("CIS-1051\pokemon.csv", "r")
    pokeFile = pokeFile.readlines()[1:152]
    for line in pokeFile:
        line = line.split(",")
        if (line[0] == "3" or line[0] == "6" or line[0] == "9"):
            pokeOptions.append(line[1].capitalize())

    drop1 = ttk.Combobox(root,state="readonly",value=pokeOptions)
    drop1.set("Pick Your Pokemon")
    drop1.bind("<<ComboboxSelected>>",lambda _ : userMS(drop1.get()))
    canvas.create_window(100,240,anchor=NW,window=drop1)

    drop2 = ttk.Combobox(root,state="readonly",value=pokeOptions)
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

    move1 = Button(root,text=userMove1,width=15,height=2,command = lambda: battleScreenUpdater(userPokemon,userMove1,"opp"))
    move2 = Button(root,text=userMove2,width=15,height=2,command = lambda: battleScreenUpdater(userPokemon,userMove2,"opp"))
    move3 = Button(root,text=userMove3,width=15,height=2,command = lambda: battleScreenUpdater(userPokemon,userMove3,"opp"))
    move4 = Button(root,text=userMove4,width=15,height=2,command = lambda: battleScreenUpdater(userPokemon,userMove4,"opp"))
    canvas.create_window(500,460,anchor=NW,window=move1)
    canvas.create_window(640,460,anchor=NW,window=move2)
    canvas.create_window(500,510,anchor=NW,window=move3)
    canvas.create_window(640,510,anchor=NW,window=move4)

    canvas.create_text(180,480,text=userPokemon,font=("Helvetica",25))
    canvas.create_line(115,515,475,515,fill="green",width=5,tags="userLine")

    oppBorderImg = PhotoImage(file="CIS-1051\moveBox.png")
    oppBorderImg = oppBorderImg.subsample(4,4)
    canvas.create_image(55,40,anchor=NW,image=oppBorderImg)

    canvas.create_text(170,90,text=oppPokemon,font=("Helvetica",20))
    canvas.create_line(110,125,400,125,fill="green",width=5,tags="oppLine")

#Screen Updater
def battleScreenUpdater(pokemon,move,player):
    global userSpeed,oppSpeed
    damageList = []
    oppMove = random.randint(0,3)
    oppMove = oppMoves[oppMove]
    damageList = damageCalculator(pokemon,move,oppMove)
    damage = damageList[0]
    oppDamage = damageList[1]
    if userSpeed > oppSpeed:
        #User Move
        hpBarUpdater(damage,player)
        #Opp Move
        hpBarUpdater(oppDamage,"user")
    elif oppSpeed > userSpeed:
        #Opp Move
        hpBarUpdater(oppDamage,"user")
        #User Move
        hpBarUpdater(damage,player)

#Damage Calculator
def damageCalculator(pokemon,move,oppMove):
    global hp,oppHp,userSpeed,oppSpeed
    #Open files/set variables
    attType = ""
    defType = ""
    power = ""
    moveType = ""
    type = []
    targetType = []
    oppAttType = ""
    oppDefType = ""
    oppPower = ""
    oppMoveType = ""
    oppType = []
    oppTargetType = []
    statsFile = open("CIS-1051\pokemon_stats.csv","r")
    statsFile = statsFile.readlines()
    monFile = open("CIS-1051\pokemon.csv","r")
    monFile = monFile.readlines()
    moveFile = open("CIS-1051\moves.csv","r")
    moveFile = moveFile.readlines()
    typeFile = open("CIS-1051\pokemon_types.csv","r")
    typeFile = typeFile.readlines()
    typeEFile = open("CIS-1051/type_efficacy.csv","r")
    typeEFile = typeEFile.readlines()
    id = 0
    oppId = 0
    hp = 0
    attack = 0
    defense = 0
    spAttack = 0
    spDefense = 0
    userSpeed = 0
    oppHp = 0
    oppAttack = 0
    oppDefense = 0
    oppSpAttack = 0
    oppSpDefense = 0
    oppSpeed = 0
    critical = 1
    stab = 1
    eff = 1
    oppCritical = 1
    oppStab = 1
    oppEff = 1
    #Get stats/ID
    for line in monFile:
        line = line.split(",")
        if line[1].capitalize() == pokemon:
            id = line[0]
            for row in statsFile:
                row = row.split(",")
                if row[0] == id:
                    if row[1] == "1":
                        hp = row[2]
                    if row[1] == "2":
                        attack = row[2]
                    if row[1] == "3":
                        defense = row[2]
                    if row[1] == "4":
                        spAttack = row[2]
                    if row[1] == "5":
                        spDefense = row[2]
                    if row[1] == "6":
                        userSpeed = row[2]
        if line[1].capitalize() == oppPokemon:
            oppId = line[0]
            for row in statsFile:
                row = row.split(",")
                if row[0] == oppId:
                    if row[1] == "1":
                        oppHp = row[2]
                    if row[1] == "2":
                        oppAttack = row[2]
                    if row[1] == "3":
                        oppDefense = row[2]
                    if row[1] == "4":
                        oppSpAttack = row[2]
                    if row[1] == "5":
                        oppSpDefense = row[2]
                    if row[1] == "6":
                        oppSpeed = row[2]
    ##User
    #Get move type
    for line in moveFile:
        line.replace("-"," ")
        line = line.split(",")
        if line[1] == move.lower():
            if line[9] == "1":
                attType = "status"
            if line[9] == "2":
                attType = attack
                defType = oppDefense
            if line[9] == "3":
                attType = spAttack
                defType = oppSpDefense
            power = line[4]
    #Crit
    critChance = random.uniform(0,100)
    if critChance < 6.25:
        critical = 2
    #STAB
    for line in typeFile:
        line = line.split(",")
        if line[0] == id:
            type.append(line[1])
    for line in moveFile:
        line = line.split(",")
        if line[1] == move.lower():
            if line[3] in type:
                stab = 1.5
    
    #Type effectiveness
    for moveLine in moveFile:
        moveLine = moveLine.split(",")
        if move.lower() == moveLine[1]:
            moveType = moveLine[3]
    for monLine in monFile:
        monLine = monLine.split(",")
        if monLine[1].capitalize() == oppPokemon:
            for typeLine in typeFile:
                typeLine = typeLine.split(",")
                if typeLine[0] == monLine[0]:
                    targetType.append(typeLine[1])
    for typeELine in typeEFile:
        typeELine = typeELine.split(",")
        if typeELine[0] == moveType and typeELine[1] in targetType:
            eff = eff * float(int(typeELine[2])/100)

    ##Opp
    #Get move type
    for line in moveFile:
        line.replace("-"," ")
        line = line.split(",")
        if line[1] == oppMove.lower():
            if line[9] == "1":
                oppAttType = "status"
            if line[9] == "2":
                oppAttType = oppAttack
                oppDefType = defense
            if line[9] == "3":
                oppAttType = oppSpAttack
                oppDefType = spDefense
            oppPower = line[4]
    #Crit
    oppCritChance = random.uniform(0,100)
    if oppCritChance < 6.25:
        oppCritical = 2
    #STAB
    for line in typeFile:
        line = line.split(",")
        if line[0] == oppId:
            oppType.append(line[1])
    for line in moveFile:
        line = line.split(",")
        if line[1] == oppMove.lower():
            if line[3] in oppType:
                oppStab = 1.5
    
    #Type effectiveness
    for moveLine in moveFile:
        moveLine = moveLine.split(",")
        if oppMove.lower() == moveLine[1]:
            oppMoveType = moveLine[3]
    for monLine in monFile:
        monLine = monLine.split(",")
        if monLine[1].capitalize() == pokemon:
            for typeLine in typeFile:
                typeLine = typeLine.split(",")
                if typeLine[0] == monLine[0]:
                    oppTargetType.append(typeLine[1])
    for typeELine in typeEFile:
        typeELine = typeELine.split(",")
        if typeELine[0] == oppMoveType and typeELine[1] in oppTargetType:
            oppEff = oppEff * float(int(typeELine[2])/100)


    damage = int((((22*float(power)*float(float(attType)/float(defType)))/50)+2)*float(critical)*float(stab)*float(eff))
    oppDamage = int((((22*float(oppPower)*float(float(oppAttType)/float(oppDefType)))/50)+2)*float(oppCritical)*float(oppStab)*float(oppEff))
    return [damage,oppDamage]

#HP Bar Updater
def hpBarUpdater(damage,player):
    global hp,changedHp,checkUser,oppHp,changedOppHp,checkOpp
    percentage = 0
    oppPercentage = 0
    color = ""
    oppColor = ""
    hpBar = 0
    oppHpBar = 0
    if player.lower() == "user":
        if checkUser:
            changedHp = hp
            checkUser = False
        changedHp = int(changedHp) - damage
        percentage = float(int(changedHp)/int(hp))
        hpBar = percentage * 360
        canvas.delete("userLine")
        if hpBar > 0:
            if percentage > 0.5:
                color = "green"
            elif percentage > 0.2:
                color = "yellow"
            elif percentage > 0:
                color = "red"
            canvas.create_line(115,515,115+hpBar,515,fill=color,width=5,tags="userLine")
    if player.lower() == "opp":
        if checkOpp:
            changedOppHp = oppHp
            checkOpp = False
        changedOppHp = int(changedOppHp) - damage
        oppPercentage = float(int(changedOppHp)/int(oppHp))
        oppHpBar = oppPercentage * 290
        canvas.delete("oppLine")
        if oppHpBar > 0:
            if oppPercentage > 0.5:
                oppColor = "green"
            elif oppPercentage > 0.2:
                oppColor = "yellow"
            elif oppPercentage > 0:
                oppColor = "red"
            canvas.create_line(110,125,110+oppHpBar,125,fill=oppColor,width=5,tags="oppLine")
        


selectionScreen()


root.mainloop()