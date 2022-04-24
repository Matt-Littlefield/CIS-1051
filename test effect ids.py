file = open("pokeapi\data/v2\csv\moves.csv","r")
file = file.readlines()
file2 = open("pokeapi\data/v2\csv\pokemon_moves.csv","r")
file2 = file2.readlines()
list = []
count = 0
for line in file2:
    line = line.split(",")
    if (line[0] == "3" or line[0] == "6" or line[0] == "9") and line[1] == "1" and line[3] == "1":
        for row in file:
            row = row.split(",")
            if row[0] == line[2]:
                if row[10] not in list and (row[2] == "1" or row[2] == "2"):
                    list.append(row[10])
print(list)
print(len(list))