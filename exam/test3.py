from csv import reader
RECIPE_FILENAME = 'recipe.txt'
def read_recipe(filename):
    ingredients = dict()
    try:
        with open(filename) as data:
            line = data.readline()
            line = data.readline().rstrip()
            print(line)
            while line != "":
                ing, qty = line.split(';')
                ingredients[ing.strip()] = {'Quantity': float(qty)}
                line = data.readline().rstrip()
    except OSError as problem:
        print(f"Yeuch: {problem}")
        exit(1)
    return ingredients

def main():
    d = read_recipe('/Users/apple/PycharmProjects/examExercises/exam/recipe.txt')
    print(d)


if __name__ == '__main__':
    main()

