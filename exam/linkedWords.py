userInput = input("Enter a word: ")
lose = False

while len(userInput) >= 2 and not lose:
    word = input("Enter next word: ")
    if word[1] == userInput[-1] and word[0] == userInput[-2]:
        userInput = word
    else:
        lose = True
        print("Game over")





