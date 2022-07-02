FILE = "fantafoot.txt"
Mgoalkeepers = 20
Mdefenders = 40
Mmidfielders = 80
Mforwards = 120

Ngoalkeepers = 3
Ndefenders = 8
Nmidfielders = 8
Nforwards = 6

def read(file):
    player = dict()
    try:
        with open(file) as infile:
            for line in infile:
                pList = line.strip().split(", ")
                player[pList[0]] = [pList[2], pList[3]]

    except OSError as problem:
        print(problem)

    return player

def role(dict1):
    goalkeepers = dict()
    defenders = dict()
    midfielders = dict()
    forwards = dict()
    for k in dict1:
        if dict1[k][0] == "goalkeeper":
            goalkeepers[k] = int(dict1[k][1])
        elif dict1[k][0] == "defender":
            defenders[k] = int(dict1[k][1])
        elif dict1[k][0] == "midfielder":
            midfielders[k] = int(dict1[k][1])
        elif dict1[k][0] == "forward":
            forwards[k] = int(dict1[k][1])

    goalkeepers = dict(sorted(goalkeepers.items(), key=lambda x: x[1], reverse=True))
    defenders = dict(sorted(defenders.items(), key=lambda x: x[1], reverse=True))
    midfielders = dict(sorted(midfielders.items(), key=lambda x: x[1], reverse=True))
    forwards = dict(sorted(forwards.items(), key=lambda x: x[1], reverse=True))

    return goalkeepers, defenders, midfielders, forwards

def buy(number, role, money):
    number1 = number
    money1 = money
    dict1 = dict()

    for k2 in role:
        if money1 - role[k2] >= number1 - 1 and number1 != 0:
            dict1[k2] = role[k2]
            number1 = number1 - 1
            money1 = money1 - role[k2]

    return dict1

def printD(dict1):
    result = " ".join(str(key) +" "+ str(value) for key, value in dict1.items())

    return result

def main():
    playerD = read(FILE)
    goalkeepers, defenders, midfielders, forwards = role(playerD)
    dictg = buy(Ngoalkeepers, goalkeepers, Mgoalkeepers)
    dictd = buy(Ndefenders, defenders, Mdefenders)
    dictm = buy(Nmidfielders, midfielders, Mmidfielders)
    dictf = buy(Nforwards, forwards, Mforwards)

    print(f"Goalkeppers: {printD(dictg)}")
    print(f"Defenders: {printD(dictd)}")
    print(f"Midfieders: {printD(dictm)}")
    print(f"Fowards: {printD(dictf)}")

main()
