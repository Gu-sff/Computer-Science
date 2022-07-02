FILE = "glucometers.txt"

def readFile(file):
    pDict = dict()

    try:
        with open(file) as infile:
            for line in infile:
                lineList = line.strip().split(" ")
                name, time, value = lineList[0], lineList[1], lineList[2]
                if int(value) >= 200:
                    if name not in pDict:
                        pDict[name] = [(time, int(value))]
                    else:
                        pDict[name] = pDict[name] + [(time, int(value))]
            pDict.keys()

    except OSError as problem:
        print(problem)

    return pDict


def findTimes(pDict):
    times = 0
    for k in pDict:
        if len(pDict[k]) > times:
            times = len(pDict[k])

    return times

def printFinal(pDict):

    while True:
        if len(list(pDict.keys())) == 0:
            break
        times = findTimes(pDict)
        for key in list(pDict.keys()):

            if len(pDict[key]) == times:
                for item in pDict[key]:
                    print(f"{key} {item[0]} {item[1]}")
                print("")
                pDict.pop(key)
            times = findTimes(pDict)

    return pDict


def main():
    pDict = readFile(FILE)
    printFinal(pDict)


if __name__ == '__main__':
    main()
