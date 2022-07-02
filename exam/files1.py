infile = open("input1.txt", "r")
outfile = open("output1.txt", "w")
newList = list()
for line in infile:
    newList.append(line)
newList.reverse()
for i in range(len(newList)):
    outfile.write(newList[i])

infile.close()
outfile.close()

