from random import random
i = 0
randomList = list()
for i in range(20):
    randomN = int(random()*100)
    randomList.append(randomN)
print(randomList)
randomList.sort()
print(randomList)




