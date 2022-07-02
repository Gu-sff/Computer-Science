from random import random
i = 0
j = 0
numberList = []
evenIndex = []
equalValue = []
equal = []
for i in range(12):
    randomNumber = int(random()*100)
    numberList.append(randomNumber)
for i in range(len(numberList)):
    if numberList[i] % 2 == 0:
        evenIndex.append(numberList[i])
    equalValue = numberList.copy()
    equalValue.remove(numberList[i])
    for j in range(len(equalValue)):
        if numberList[i] == equalValue[j] and numberList[i] not in equal:
            equal.append(numberList[i])
reversed = numberList.copy()
reversed.reverse()
print(numberList)
print(evenIndex, "\n")
print(equal, "\n")
print(reversed, "\n")
print("first: ", numberList[0], "last: ", numberList[len(numberList)-1])


