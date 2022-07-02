numberList = list()
localMax = list()
userInput = input("Enter a integer: ")
while not userInput.isspace():
  numberList.append(int(userInput))
  userInput = input("Enter a integer: ")
for i in range(1,len(numberList)-1):
    if numberList[i] > numberList[i-1] and numberList[i] > numberList[i+1]:
        localMax.append(numberList[i])
if len(localMax) == 0:
    print("No maxima")
else:
    print(localMax)



