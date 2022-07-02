infile = open("products.txt", "r")
dictionary = {}

line = infile.readline()
while line != "":
    newline = line.split()
    dictionary[newline[0]] = newline[1]
    line = infile.readline()

infile1 = open("purchases.txt", "r")
line1 = infile1.readline()
suspicious = list()

while line1 != "":
    newline1 = line1.split()
    if newline1[1] != dictionary[newline1[0]]:
        suspicious.append(newline1[0])
    line1 = infile1.readline()

print("Suspicious transactions list")
for i in range(len(suspicious)):
    print(f"Product code: {suspicious[i]}")
    print(f"Official dealer: {dictionary[suspicious[i]]}")
    print(" ")


