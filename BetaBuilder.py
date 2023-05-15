import json
import os
import numpy as np
import math
import csv
from compData import compData

moveNames = []
moveCats = []
movePows = []
moveAccs = []
moveTypes = []
learnsets = []

with open(os.getcwd() + '/resources/learnsets.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        learnsets.append(row[1:len(row)])

with open(os.getcwd() + '/resources/moves.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        moveNames.append(row[1])
        moveCats.append(row[7])
        movePows.append(row[8])
        moveAccs.append(row[9])
        moveTypes.append(row[5])

for i in range(len(moveTypes)):
    if moveTypes[i] == '0':
        moveTypes[i] = "Normal"
    elif moveTypes[i] == '1':
        moveTypes[i] = "Fighting"
    elif moveTypes[i] == '2':
        moveTypes[i] = "Flying"
    elif moveTypes[i] == '3':
        moveTypes[i] = "Poison"
    elif moveTypes[i] == '4':
        moveTypes[i] = "Ground"
    elif moveTypes[i] == '5':
        moveTypes[i] = "Rock"
    elif moveTypes[i] == '6':
        moveTypes[i] = "Bug"
    elif moveTypes[i] == '7':
        moveTypes[i] = "Ghost"
    elif moveTypes[i] == '8':
        moveTypes[i] = "Steel"
    elif moveTypes[i] == '9':
        moveTypes[i] = "Fire"
    elif moveTypes[i] == '10':
        moveTypes[i] = "Water"
    elif moveTypes[i] == '11':
        moveTypes[i] = "Grass"
    elif moveTypes[i] == '12':
        moveTypes[i] = "Electric"
    elif moveTypes[i] == '13':
        moveTypes[i] = "Psychic"
    elif moveTypes[i] == '14':
        moveTypes[i] = "Ice"
    elif moveTypes[i] == '15':
        moveTypes[i] = "Dragon"
    elif moveTypes[i] == '16':
        moveTypes[i] = "Dark"
    elif moveTypes[i] == '17':
        moveTypes[i] = "Fairy"

## col: 0 = index, 1 = name, 5 = type, 7 = category, 8 = power, 9 = accuracy
## BREAK
## silvally is default to only normal type

with open(os.getcwd() + '/resources/pokemon.json') as f:
    data = json.load(f)

names = []
types = []
stats = []

pokemon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

da = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 / 2, 0, 1, 1, 1 / 2, 1],
               [1, 1 / 2, 1 / 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1 / 2, 1, 1 / 2, 1, 2, 1],
               [1, 2, 1 / 2, 1, 1 / 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1 / 2, 1, 1, 1],
               [1, 1, 2, 1 / 2, 1 / 2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1 / 2, 1, 1, 1],
               [1, 1 / 2, 2, 1, 1 / 2, 1, 1, 1 / 2, 2, 1 / 2, 1, 1 / 2, 2, 1, 1 / 2, 1, 1 / 2, 1],
               [1, 1 / 2, 1 / 2, 1, 2, 1 / 2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1 / 2, 1],
               [2, 1, 1, 1, 1, 2, 1, 1 / 2, 1, 1 / 2, 1 / 2, 1 / 2, 2, 0, 1, 2, 2, 1 / 2],
               [1, 1, 1, 1, 2, 1, 1, 1 / 2, 1 / 2, 1, 1, 1, 1 / 2, 1 / 2, 1, 1, 0, 2],
               [1, 2, 1, 2, 1 / 2, 1, 1, 2, 1, 0, 1, 1 / 2, 2, 1, 1, 1, 2, 1],
               [1, 1, 1, 1 / 2, 2, 1, 2, 1, 1, 1, 1, 2, 1 / 2, 1, 1, 1, 1 / 2, 1],
               [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1 / 2, 1, 1, 1, 1, 0, 1 / 2, 1],
               [1, 1 / 2, 1, 1, 2, 1, 1 / 2, 1 / 2, 1, 1 / 2, 2, 1, 1, 1 / 2, 1, 2, 1 / 2, 1 / 2],
               [1, 2, 1, 1, 1, 2, 1 / 2, 1, 1 / 2, 2, 1, 2, 1, 1, 1, 1, 1 / 2, 1],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1 / 2, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1 / 2, 0],
               [1, 1, 1, 1, 1, 1, 1 / 2, 1, 1, 1, 2, 1, 1, 2, 1, 1 / 2, 1, 1 / 2],
               [1, 1 / 2, 1 / 2, 1 / 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1 / 2, 2],
               [1, 1 / 2, 1, 1, 1, 1, 2, 1 / 2, 1, 1, 1, 1, 1, 1, 2, 2, 1 / 2, 1]])

for i in compData:
    names.append(i.get("xname"))

for i in range(len(data) - 1):
    types.append(data[i]['types'])

for i in range(len(data) - 1):
    stats.append(data[i]['base_stats'])


def getBp(move):
    return int(movePows[moveNames.index(move)])


def getAcc(move):
    return int(moveAccs[moveNames.index(move)])


def physOrSpec(move):
    if moveCats[moveNames.index(move)] == '1':
        return ("phys")
    elif moveCats[moveNames.index(move)] == '2':
        return ("spec")
    else:
        return ("stat")



def weaknesses(type):
    toReturn = []
    for i in range(18):
        if da.item((i, pokemon_types.index(type))) >= 2.0:
            toReturn.append(pokemon_types[i])
    return toReturn


def isCompatible(pokemon, move):
    moves = []
    for learnset in learnsets:
        for item in learnset:
            if pokemon in item:
                moves.append(learnset[0])
    for i in moves:
        if i == move:
            return True
    return False


def getWeak(pokemon):
    weaknesses = []
    t1m = []
    t2m = []
    index = names.index(pokemon)
    typing = types[index]
    typeIndex = 0

    if len(typing) > 1:
        typeIndex = pokemon_types.index(typing[0])
        for i in range(18):
            t1m.append(da.item((i, typeIndex)))
        typeIndex = pokemon_types.index(typing[1])
        for i in range(18):
            t2m.append(da.item((i, typeIndex)))
            weaknesses.append(t1m[i] * t2m[i])

    else:
        typeIndex = pokemon_types.index(typing[0])
        for i in range(18):
            t1m.append(da.item((i, typeIndex)))
            weaknesses.append(t1m[i])
    return weaknesses


def getMoveType(move):
    return moveTypes[moveNames.index(move)]


def getType(pokemon):
    return types[names.index(pokemon)]


def getStats(pokemon):
    return stats[names.index(pokemon)]


def dupeTypeCheck(list):
    templist = ['', '', '', '', '']
    for i in range(len(templist)):
        templist[i] = getType(list[i])[0]

    for elem in templist:
        if templist.count(elem) > 1:
            return True
    return False


def getBst(pokemon):
    bst = 0
    for i in getStats(pokemon):
        bst += i
    return bst


def revMon(list):
    bsts = []
    for i in list:
        bsts.append(getBst(i))
    temp = 0
    for i in bsts:
        if i > temp:
            temp = i
    highBst = bsts.index(temp)
    list.pop(highBst)


def addMon(list):
    totals = []
    for mon in list:
        bst = 0
        for i in getStats(mon):
            bst += i
        totals.append(bst)
    temp = 0
    tempIndex = 0
    for stat in totals:
        if stat > temp:
            temp = stat
            tempIndex = totals.index(temp)
    a = list.pop(tempIndex)
    ## b = totals.pop(tempIndex)
    return (a)


def replace(list, list2):
    revMon(list)
    list.append(addMon(list2))


def replaceDupes(list, list2):
    indivTypes = []

    if dupeTypeCheck(list):
        for i in range(len(list)):
            indivTypes.append(getType(list[i])[0])

    dupetype = ''
    strTemp = ''
    for type in indivTypes:
        if type != strTemp:
            strTemp = type
        elif type == strTemp:
            dupetype = type
            break

    firstInstance = ''

    for i in list:
        if getType(i)[0] == dupetype:
            firstInstance = i
            break

    for i in range(5):
        for i in list:
            if getType(i)[0] == dupetype and i != firstInstance:
                list.remove(i)

    for i in range(5 - len(list)):
        list.append(addMon(list2))


def getHighAtk(pokemon):
    if getStats(pokemon)[1] > getStats(pokemon)[3]:
        return ("atk")
    elif getStats(pokemon)[3] > getStats(pokemon)[1]:
        return ("spatk")
    else:
        return "same"

def getHighestStat(pokemon): ## 0 = HP, 1 = atk, 2 = def, 3 = spA, 4 = spD, 5 = spe
    temp = 0
    tempindex = 0
    for i in range(len(getStats(pokemon))):
        if getStats(pokemon)[i] > temp:
            tempindex = i
            temp = getStats(pokemon)[i]
    return tempindex


def getMove(pokemon, moveset, cat):
    compMoves = []
    for move in moveNames:
        if isCompatible(pokemon, move):
            compMoves.append(move)

def getHighDef(pokemon):
    if getStats(pokemon)[2] > getStats(pokemon)[4]:
        return "def"
    elif getStats(pokemon)[4] > getStats(pokemon)[2]:
        return "spdef"
    else:
        return "same"


def synergyBuild(requiredMon, list, dimension, count):
    if dimension < count:
        reqMonWeak = getWeak(requiredMon)
        for mon in names:
            temp = getWeak(mon)
            for i in range(18):
                if temp[i] < 1 and reqMonWeak[i] > 1:
                    list.append(mon)
                    dimension += 1
                    synergyBuild(mon, list, dimension, count)
    return list


def refine(list):
    teams2 = []
    for i in list:
        if i not in teams2 and list.count(i) > 1:
            teams2.append(i)

    return teams2


def getText(mon):
    link = f"""https://www.pikalytics.com/pokedex/ss/{mon}"""
    html = requests.get(link).text
    parsed_html = BeautifulSoup(html, features="html.parser")
    toReturn = []
    for item in parsed_html.body.find_all(class_="pokedex-move-entry-new"):
        toReturn.append(item.text)
    return toReturn


def getTeam(requiredMon, slide, count):
    if count.get() == 0:
        counter = 1
    else:
        counter = 6 - ((math.floor(math.floor(count.get() - 100) / 50)) + 1)

    teams2 = refine(synergyBuild(requiredMon, [], 0, counter))

    totals = []

    for mon in teams2:
        bst = 0
        for i in getStats(mon):
            bst += i
        totals.append(bst)

    toReturn = []

    for i in range(5):
        temp = 0
        tempIndex = 0
        for stat in totals:
            if stat > temp:
                temp = stat
                tempIndex = totals.index(temp)

        toReturn.append(teams2[tempIndex])

        del teams2[tempIndex]

        del totals[tempIndex]

    if slide.get() == 0:
        slider = 1
    else:
        slider = (math.floor(math.floor(slide.get() - 100) / 50)) + 1

    if slider < 5:
        for i in range(5 * (3 - slider)):
            replace(toReturn, teams2)

    replaceDupes(toReturn, teams2)
    toReturn.append(requiredMon)

#    for mon in toReturn:
#        for dataSet in compData:

    toReturnStr = ""
    toReturnData = []

    for pokemon in toReturn:
        for data in compData:
            if data.get("xname") == pokemon:
                toReturnData.append(pokemon)
                if " ".join(data.get("items")[0].split(" ")[:-1]) in toReturnData:
                    toReturnData.append(" ".join(data.get("items")[1].split(" ")[:-1]))
                else:
                    toReturnData.append(" ".join(data.get("items")[0].split(" ")[:-1]))
                toReturnData.append(" ".join(data.get("xabilities")[0].split(" ")[:-1]))
                toReturnData.append(data.get("spreads")[0].split(" ")[0].split(":")[1])
                toReturnData.append(data.get("spreads")[0].split(" ")[0].split(":")[0])
                toReturnData.append([" ".join(z.split(" ")[:-1]) for z in data.get("moves")])

    j = 0
    for i in range(6):
        toReturnStr += toReturnData[0 + j] + " @ " + toReturnData[1 + j] + "\n"
        toReturnStr += "Ability: " + toReturnData[2 + j] + "\n"
        toReturnStr += "Level: 50\n"
        toReturnStr += "EVs: "
        evsSplit = toReturnData[3+j].split("/")
        for k in range(len(evsSplit)):
            if k == 0:
                toReturnStr += evsSplit[k] + " HP / "
            elif k == 1:
                toReturnStr += evsSplit[k] + " Atk / "
            elif k == 2:
                toReturnStr += evsSplit[k] + " Def / "
            elif k == 3:
                toReturnStr += evsSplit[k] + " SpA / "
            elif k == 4:
                toReturnStr += evsSplit[k] + " SpD / "
            elif k == 5:
                toReturnStr += evsSplit[k] + " Spe\n"
        toReturnStr += toReturnData[4 + j] + " Nature\n"
        for i in toReturnData[5 + j]:
            toReturnStr += "- " + i + "\n"
        toReturnStr += "\n"
        j += 6

    return toReturnStr

