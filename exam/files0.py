infile = open("input.txt", "r")
outfile = open("output.txt", "w")
line = infile.readline()
count = 1
while line != "":
    outfile.write(f"/*{count}*/{line}")
    line = infile.readline()
    count = count + 1
    print(line)


infile.close()
outfile.close()

print(outfile)



