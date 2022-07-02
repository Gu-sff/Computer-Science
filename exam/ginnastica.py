SCORES = "scores.txt"

def readScores(file):
    female = dict()
    countries = dict()
    try:
        with open(file) as infile:
            for line in infile:
                firstname, surename, sex, nation, score = line.strip().split(" ", 4)
                listS = score.split(" ")
                scoreList = [float(i) for i in listS]
                totalScore = round(sumScore(scoreList), 1)
                if sex == "F":
                    female[firstname + " "+ surename] = nation, totalScore
                if nation in countries:
                    countries[nation] = countries[nation] + totalScore
                else:
                    countries[nation] = totalScore

    except OSError as problem:
        print(problem)

    return female, countries

def sumScore(scoreList):
    newList = sorted(scoreList)
    newList.remove(newList[0])
    newList.remove(newList[len(newList)-1])
    score = sum(newList)
    return score

def findFwinner(dict1):
    best = 0
    bPlayer = ''
    country = ''
    for k in dict1:
        if dict1[k][1] > best:
            best = dict1[k][1]
    sort = dict(sorted(dict1.items(), reverse=True))
    for key in sort:
        if dict1[key][1] == best:
            bPlayer = key
            country = dict1[key][0]
    return bPlayer, country, best


def findTopCountry(dict):
    top = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    topThree = top[:3]
    return topThree

def printM(fWinner, topC):
    print("Female winner: ")
    print(f"{fWinner[0]}, {fWinner[1]} - Score: {fWinner[2]}")
    print("\nOverall nations ranking: ")
    for item in topC:
        print(f"1) {item[0]} - Total score: {item[1]}")

def main():
    femailD, countriesD = readScores(SCORES)
    fWinner = findFwinner(femailD)
    topCounties = findTopCountry(countriesD)
    printM(fWinner, topCounties)



if __name__ == '__main__':
    main()
