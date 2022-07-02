DATES = "dates.txt"
RULES = "rules.txt"

def format(string):
    d, m, y = string.split("-")
    return int(y), int(m), int(d)

def readDate(dates,listRule):
    try:
        with open(dates) as datesFile:
            for line in datesFile:
                date = format(line.strip())
                ruleSet = compare(date, listRule)
                printResult(line.strip(), ruleSet)

    except OSError as problem:
        print(f"Error {problem}")

def readRules(file):
    listRule = list()
    try:
        with open(file) as rules:
            for line in rules:
                inSet = set()
                outSet = set()
                date, info = line.strip().split(": ")
                fDate = format(date)
                newInfo = info.split(" ")
                for n in newInfo:
                    if n[0] == "+":
                        inSet.add(n[1:])
                    elif n[0] == "-":
                        outSet.add(n[1:])
                listRule.append((fDate, inSet, outSet))

    except OSError as problem:
        print(f"Error: {problem}")

    return listRule

def compare(date, listRule):
    finalSet = set()
    for rD, i, o in listRule:
        if rD <= date:
            for item in i:
                finalSet.add(item)
            for item in o:
                finalSet.remove(item)

    return finalSet


def printResult(date, ruleSet):
    print(f"{date}: ")
    for i in ruleSet:
        print(i)


def main():
    listRule = readRules(RULES)
    readDate(DATES, listRule)



if __name__ == '__main__':
    main()
