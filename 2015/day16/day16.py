puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day16/day16.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

truesue = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]

def inputlist(input :str) -> list:
    list = []
    for line in input.split('\n'):
        strings = line.split(' ')
        # always 3 things remembered about sue
        children = None
        cats = None
        samoyeds = None
        pomeranians = None
        akitas = None
        vizslas = None
        goldfish = None
        trees = None
        cars = None
        perfumes = None

        match strings[2]:
            case 'children:':
                children = int(strings[3].removesuffix(','))
            case 'cats:':
                cats = int(strings[3].removesuffix(','))
            case 'samoyeds:':
                samoyeds = int(strings[3].removesuffix(','))
            case 'pomeranians:':
                pomeranians = int(strings[3].removesuffix(','))
            case 'akitas:':
                akitas = int(strings[3].removesuffix(','))
            case 'vizslas:':
                vizslas = int(strings[3].removesuffix(','))
            case 'goldfish:':
                goldfish = int(strings[3].removesuffix(','))
            case 'trees:':
                trees = int(strings[3].removesuffix(','))
            case 'cars:':
                cars = int(strings[3].removesuffix(','))
            case 'perfumes:':
                perfumes = int(strings[3].removesuffix(','))
        match strings[4]:
            case 'children:':
                children = int(strings[5].removesuffix(','))
            case 'cats:':
                cats = int(strings[5].removesuffix(','))
            case 'samoyeds:':
                samoyeds = int(strings[5].removesuffix(','))
            case 'pomeranians:':
                pomeranians = int(strings[5].removesuffix(','))
            case 'akitas:':
                akitas = int(strings[5].removesuffix(','))
            case 'vizslas:':
                vizslas = int(strings[5].removesuffix(','))
            case 'goldfish:':
                goldfish = int(strings[5].removesuffix(','))
            case 'trees:':
                trees = int(strings[5].removesuffix(','))
            case 'cars:':
                cars = int(strings[5].removesuffix(','))
            case 'perfumes:':
                perfumes = int(strings[5].removesuffix(','))
        match strings[6]:
            case 'children:':
                children = int(strings[7])
            case 'cats:':
                cats = int(strings[7])
            case 'samoyeds:':
                samoyeds = int(strings[7])
            case 'pomeranians:':
                pomeranians = int(strings[7])
            case 'akitas:':
                akitas = int(strings[7])
            case 'vizslas:':
                vizslas = int(strings[7])
            case 'goldfish:':
                goldfish = int(strings[7])
            case 'trees:':
                trees = int(strings[7])
            case 'cars:':
                cars = int(strings[7])
            case 'perfumes:':
                perfumes = int(strings[7])
        list.append([children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes])
    return list

def part1():
    list = inputlist(puzzleinput)
    for i in range(1, 501):
        matches = 0
        for j in range(0, len(list[i-1])):
            if list[i-1][j] == truesue[j]:
                matches += 1
        if matches == 3:
            print(i)
    print()

def part2():
    list = inputlist(puzzleinput)
    for i in range(1, 501):
        matches = 0
        if list[i-1][0] != None and list[i-1][0] == truesue[0]:
            matches += 1
        if list[i-1][1] != None and list[i-1][1] > truesue[1]:
            matches += 1
        if list[i-1][2] != None and list[i-1][2] == truesue[2]:
            matches += 1
        if list[i-1][3] != None and list[i-1][3] < truesue[3]:
            matches += 1
        if list[i-1][4] != None and list[i-1][4] == truesue[4]:
            matches += 1
        if list[i-1][5] != None and list[i-1][5] == truesue[5]:
            matches += 1
        if list[i-1][6] != None and list[i-1][6] < truesue[6]:
            matches += 1
        if list[i-1][7] != None and list[i-1][7] > truesue[7]:
            matches += 1
        if list[i-1][8] != None and list[i-1][8] == truesue[8]:
            matches += 1
        if list[i-1][9] != None and list[i-1][9] == truesue[9]:
            matches += 1
        if matches == 3:
            print(i)
    print()

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")