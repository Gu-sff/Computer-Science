QUESTION1 = "q1.txt"
QUESTION2 = "q2.txt"
CHARA = "chara.txt"

def readFirstLine(file):
    list1 = list()
    try:
        with open(file) as infile:
            list1 = infile.readline().rstrip().split(";")
    except OSError:
        print("Error")

    return list1

def readFile(file):
    charaDict = dict()
    try:
        with open(file) as infile:
            infile.readline()
            for line in infile:
                listChara = line.rstrip().split(";")
                charaDict[listChara[0]] = list()
                for i in range(1, len(listChara)):
                    charaDict[listChara[0]].append(listChara[i])
    except OSError as problem:
        print(f"Error: {problem}")
    return charaDict

def readQuesiton(file):
    questionDict = dict()
    try:
        with open(file) as questionFile:
            for line in questionFile:
                question, value = line.rstrip().split(" = ", 1)
                questionDict[question] = value
    except OSError as problem:
        print(f"Error: {problem}")

    return questionDict

def compare(file,question, fistLine):
    for i in range(1, len(fistLine)):
        if fistLine[i] in question:
            for key in file:
                valueList = file[key]
                value = valueList[i-1]
        if value == question[fistLine[i]]:
            print(f"{key}- {valueList}")

def main():
    dictfile = readFile(CHARA)
    dictQuestion = readQuesiton(QUESTION2)
    firstLine = readFirstLine(CHARA)
    print(dictfile)
    print(dictQuestion)
    print(firstLine)
    print(compare(dictfile, dictQuestion, firstLine))


main()
