from csv import DictReader
characters = dict()
try:
    with open("chara.txt", newline='') as raw_data:
        for d in DictReader(raw_data, delimiter=';'):
                name = d['Name']
                del d['Name']
                characters[name] = d
        print(characters)

except OSError as problem:
    print(f"Error:{problem}")

