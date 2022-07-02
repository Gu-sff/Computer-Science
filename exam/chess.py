PLAYERS = "pShort.txt"
GAMES = "gShort.txt"

def readPlayer(player):
    dictPlayer = dict()
    try:
        with open(player) as infile:
            infile.readline()
            for line in infile:
                name, selo = line.strip().split(",")
                dictPlayer[name] = int(selo)

    except OSError as problem:
        print(problem)

    return dictPlayer

def readGame(game, dictPlayer):
    try:
        with open(game) as infile:
            infile.readline()
            for line in infile:
                player1, player2, result = line.strip().split(",")
                betterResult = result.split("-")
                if int(betterResult[0]) > int(betterResult[1]):
                    winner = player1
                    loser = player2
                elif int(betterResult[0]) < int(betterResult[1]):
                    winner = player2
                    loser = player1
                update(winner, loser, dictPlayer)

    except OSError as problem:
        print(problem)

    return dictPlayer


def delta(player_1, player_2):
    return 1 / (1 + 2**((player_1 - player_2) / 100))


def update(winner, loser, dictPlayer):
    if winner not in dictPlayer:
        dictPlayer[winner] = 1500
    if loser not in dictPlayer:
        dictPlayer[loser] = 1500
    updateW = dictPlayer[winner] + 200*delta(dictPlayer[winner], dictPlayer[loser])
    updateL = dictPlayer[loser] - 200*delta(dictPlayer[winner], dictPlayer[loser])
    dictPlayer[winner] = round(updateW)
    dictPlayer[loser] = round(updateL)


def printD(dict):
    for k in dict:
        print(': '.join((str(k), str(dict[k]))))

def main():
    dictPlayer = readPlayer(PLAYERS)
    newDict = readGame(GAMES, dictPlayer)
    printD(newDict)

if __name__ == '__main__':
    main()
