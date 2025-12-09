puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day15/day15.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

def getinputlist(input :str) -> list:
    list = []
    for line in input.split('\n'):
        strings = line.split(' ')
        name = strings[0].removesuffix(':')
        capacity = int(strings[2].removesuffix(','))
        durability = int(strings[4].removesuffix(','))
        flavour = int(strings[6].removesuffix(','))
        texture = int(strings[8].removesuffix(','))
        calories = int(strings[10])
        #              0       1          2         3        4        5
        list.append([name, capacity, durability, flavour, texture, calories])
    return list

def getitem(list :list, string :str) -> list:
    for item in list:
        if item[0] == string:
            return item

def part1():
    list = getinputlist(puzzleinput)
    print(list)
    bestscore = 0
    for i in range(0, 101):
        for j in range(0, 101):
            for k in range(0, 101):
                l = 100 - i - j - k
                if i + j + k + l != 100:
                    continue
                capacity = max(i*list[0][1] + j*list[1][1] + k*list[2][1] + l*list[3][1], 0)
                durability = max(i*list[0][2] + j*list[1][2] + k*list[2][2] + l*list[3][2], 0)
                flavour = max(i*list[0][3] + j*list[1][3] + k*list[2][3] + l*list[3][3], 0)
                texture = max(i*list[0][4] + j*list[1][4] + k*list[2][4] + l*list[3][4], 0)
                score = capacity * durability * flavour * texture
                if score > bestscore:
                    bestscore = score

    print(bestscore)

def part2():
    list = getinputlist(puzzleinput)
    print(list)
    bestscore = 0
    for i in range(0, 101):
        for j in range(0, 101):
            for k in range(0, 101):
                l = 100 - i - j - k
                if i + j + k + l != 100:
                    continue
                capacity = max(i*list[0][1] + j*list[1][1] + k*list[2][1] + l*list[3][1], 0)
                durability = max(i*list[0][2] + j*list[1][2] + k*list[2][2] + l*list[3][2], 0)
                flavour = max(i*list[0][3] + j*list[1][3] + k*list[2][3] + l*list[3][3], 0)
                texture = max(i*list[0][4] + j*list[1][4] + k*list[2][4] + l*list[3][4], 0)
                calories = max(i*list[0][5] + j*list[1][5] + k*list[2][5] + l*list[3][5], 0)
                if calories != 500:
                    continue
                score = capacity * durability * flavour * texture
                if score > bestscore:
                    bestscore = score

    print(bestscore)

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")