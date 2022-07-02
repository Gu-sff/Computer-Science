userInput = input("Enter a sequence of numbers: ")
string = userInput.rstrip()
string1 = string.split(" ")

print(string1)
i = 0
numbers = []
for i in range(len(string1)):
    numbers.append(int(string1[i]))

for i in range(len(numbers)):
    if i % 2 != 0:
        numbers[i] = -numbers[i]

print(sum)



