import pprint
QUESTION1 = "q1.txt"
QUESTION2 = "q2.txt"
CHARA = "chara.txt"

def read(file, q):
    finalList = list()
    try:
        with open(file) as infile:
            firstLine1 = firstLine(file)
            for line in infile:
                togetherlList = list()
                lineList = line.strip().split(";")
                togetherlList.append(lineList[0])
                for i in range(1, len(firstLine1)):
                    togetherlList.append((firstLine1[i], lineList[i]))
                if compare(q, togetherlList) == True:
                   finalList.append(togetherlList)

    except OSError as problem:
        print(f"Error: {problem}")

    return finalList

def firstLine(file):
    try:
        with open(file) as first:
            firstLine = first.readline().strip().split(";")

    except OSError as prpoblem:
        print(f"Error: {prpoblem}")
    return firstLine

def readIndex(question):
    qList = list()
    try:
        with open(question) as questionFile:
            for line in questionFile:
                q1, q2 = line.strip().split(" = ")
                qList.append((q1, q2))

    except OSError as prpoblem:
        print(f"Error: {prpoblem}")

    return qList


def compare(q, list2):
    if q in list2:
        return True


def main():
    qList = readIndex(QUESTION1)
    count = 1
    temList = list()
    for i in range(len(qList)):
        q = qList[i]
        finList = read(CHARA, q)
        if count != 1:
            temppoo = list()
            for o in range(len(temList)):
                if temList[o] in finList:
                    temppoo.append(temList[o])
            finList = temppoo
        temList = finList

        print(f"Step {count} - question: {q[0]} = {q[1]}\n Selected characters: ")
        count = count + 1
        tem = list()
        for j in range(len(finList)):
            tem2 = finList[j]
            string = f"{tem2[0]} - "
            tem.append(string)
            for k in range(1, len(tem2)):
                tem3 = tem2[k]
                string = string + f"{tem3[0]}: {tem3[1]}, "
            print(string.strip(", "))

    if len(tem) == 1:
        print("You win!")
    else:
        print("Too bad you lose.")


main()
