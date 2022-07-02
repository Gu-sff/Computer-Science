STARTINGLISTA = [1,4,9,6,12]
STARTINGLISTB = [9,7,4,9,11,15]

def merage(a, b):
    newlist = list()
    if len(STARTINGLISTA) > len(STARTINGLISTB):
        for i in range(len(STARTINGLISTB)):
            newlist.append(STARTINGLISTA[i])
            newlist.append(STARTINGLISTB[i])
        for j in range(len(STARTINGLISTB), len(STARTINGLISTA)):
            newlist.append(STARTINGLISTA[j])
    elif len(STARTINGLISTA) < len(STARTINGLISTB):
        for i in range(len(STARTINGLISTA)):
            newlist.append(STARTINGLISTA[i])
            newlist.append(STARTINGLISTB[i])
        for k in range(len(STARTINGLISTA), len(STARTINGLISTB)):
            newlist.append(STARTINGLISTB[k])
    return newlist

def main():
    resultList = merage(STARTINGLISTA, STARTINGLISTB)
    print(resultList)


if __name__ == "__main__":
    main()
