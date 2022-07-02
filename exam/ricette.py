RECIPE = "recipe.txt"
FOODS = "foods.txt"

def readRecipe(file):
    count = 0
    totalCost = 0
    totalCalories = 0
    try:
        with open(file) as infile:
            line = infile.readline()
            print(line.strip())
            line = infile.readline().rstrip()
            while line != "":
                count = count + 1
                item, g0 = line.split("; ")
                line = infile.readline().strip()
                g = float(g0)
                co, ca = cC(item, g, FOODS)
                totalCost = totalCost + co
                totalCalories = totalCalories + ca
                print(f"{item} - {g}")

            print(f"\nNumber of ingredients: {count}")
            print(f"Recipe cost: {round(totalCost,2)}")
            print(F"Recipe calories: {round(totalCalories,2)}")

    except OSError as problem:
        print(f"Error: {problem}")

def cC(item, g, food):
    fialP = 0
    fianlC = 0
    dFood = dict()
    try:
        with open(food) as foodFile:
            for line in foodFile:
                item0, p, c = line.strip().split("; ")
                dFood[item0] = float(p), float(c)
            for k in dFood:
                price = dFood[k][0]
                cal = dFood[k][1]
                if item == k:
                    fialP = g*0.001*price
                    fianlC = g*0.001*cal
        return fialP, fianlC

    except OSError as problem:
        print(problem)


def main():
    readRecipe(RECIPE)

if __name__ == '__main__':
    main()
