FILE = "map.txt"

def readMatrix(file):
    matrix = list()
    try:
        with open(file) as infile:
            for line in infile:
                temList = list()
                list0 = line.strip().split(" ")
                for number in list0:
                    temList.append(int(number))
                matrix.append(temList)



    except OSError as problem:
        print(f"Error: {problem}")

    return matrix

def findPeak(matrix):
    peak = list()

    for row in range(len(matrix)):
        rowLength = len(matrix[row])
        for col in range(rowLength):
            tempRowU = 0
            tempRowD = 0
            tempColL = 0
            tempColR = 0
            if row - 1 != -1:
                tempRowU = matrix[row-1][col]
            if row + 1 < len(matrix):
                tempRowD = matrix[row+1][col]
            if col - 1 != -1:
                tempColL = matrix[row][col-1]
            if col + 1 < rowLength:
                tempColR = matrix[row][col+1]

            if matrix[row][col] > tempRowU and matrix[row][col] > tempRowD and matrix[row][col] > tempColL and matrix[row][col] > tempColR:
                peak.append((matrix[row][col], row, col))

    return peak

def averageH(peak):
    average = 0
    count = 0
    listH = list()
    for i in range(len(peak)):
        count = count + 1
        h, r, c = peak[i]
        listH.append(h)
    average = sum(listH)/count

    return average

def printPeak(peak):
    average = averageH(peak)
    for i in range(len(peak)):
        h, r, c = peak[i]
        print(f"{h} {r} {c}")
    print(f"\nAverage height: {average}m")


def main():
    matrix = readMatrix(FILE)
    peak = findPeak(matrix)
    printPeak(peak)


if __name__ == '__main__':
    main()
