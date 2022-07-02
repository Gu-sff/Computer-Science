try:
    playerDict = dict()
    with open("/Users/apple/PycharmProjects/examExercises/exam/bowling.txt") as infile:
        for line in infile:
            player, score = line.strip().split(";", 1)
            playerDict[player] = score
    print(playerDict)


except OSError as problem:
    print(f"Error: {problem}")
