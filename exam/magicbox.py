ACTION = "actions.txt"
NUMBER = 2

def read(action):
    magicBox = dict()
    boxCount = 0
    try:
        with open(action) as infile:
            for line in infile:
                newList = line.strip().split(" ")
                actions, item = newList[0], newList[3]
                if actions == "Bob":
                    if item in magicBox:
                        magicBox[item] = magicBox[item] + 1
                    elif boxCount < NUMBER:
                        magicBox[item] = 1
                        boxCount = boxCount + 1
                    elif boxCount >= NUMBER:
                        print(f"Error, because Alice can not store {item}")
                elif actions == "Carl":
                    if item in magicBox:
                        magicBox[item] = magicBox[item] - 1
                        if magicBox[item] == 0:
                            magicBox.pop(item)
                            boxCount = boxCount -1
                    elif item not in magicBox:
                        print(f"Error, because Alice can not give {item}")

    except OSError as problem:
        print(f"Error: {problem}")

def main():
    read(ACTION)


if __name__ == '__main__':
    main()
