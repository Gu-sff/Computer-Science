fileName = "bowling.txt"

def read(file):
    player = dict()
    try:
        with open(file) as infile:
            for line in infile:
                lineList = line.strip().split(";")
                name = lineList[0] + " " + lineList[1]
                lineList.remove(lineList[0])
                lineList.remove(lineList[0])
                player[name] = lineList

    except OSError as problem:
        print(f"Error: {problem}")

    return player


def compare(player):
    totalPoints = dict()
    for key in player:
        list = player[key]
        newList = []
        for i in range(len(list)):
            intL = int(list[i])
            newList.append(intL)
        totalPoints[key] = sum(newList)
    rank = sorted(totalPoints.items(), key=lambda x: x[1], reverse=True)
    return rank



def theMost(playerDict):
    sumDict = dict()
    mostTen = 0
    mostZero = 0
    zeroPlayer = ""
    tenPlayer = ""

    for key in playerDict:
        tenS = 0
        zeroS = 0
        vList = playerDict[key]
        rlist10 = list()
        rlist0 = list()
        for i in range(len(vList)):
            if vList[i] == "10":
                tenS = tenS + 1
            if  vList[i] == "0":
                zeroS = zeroS + 1
        sumDict[key] = (zeroS, tenS)
    for k in sumDict:
        v = sumDict[k]
        if v[0] >= mostZero:
            mostZero = v[0]
        if v[1] >= mostTen:
            mostTen = v[1]

    for k1 in sumDict:
        v1 = sumDict[k1]
        if v1[0] == mostZero:
            zeroPlayer = k1
        if v1[1] == mostTen:
            tenPlayer = k1
    rlist0.append(zeroPlayer)
    rlist0.append(sumDict[zeroPlayer][0])
    rlist10.append(tenPlayer)
    rlist10.append(sumDict[tenPlayer][1])


    return rlist0,rlist10


def main():
    player = read(fileName)
    most0, most10 = theMost(player)
    rank = compare(player)
    for i in range(len(rank)):
        list = rank[i]
        print(f"{list[0]} {list[1]}")

    print(f"{most10[0]} has knocked down all the pins {most10[1]} times")
    print(f"{most0[0]} has missed {most0[1]} times")


main()

