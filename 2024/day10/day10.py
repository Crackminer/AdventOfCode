puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day10/day10.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

testinput = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def findnumtrails(list :list, y :int, x :int) -> list:
    if list[y][x] == 9:
        return [[y, x]]
    l = []
    if x+1 < len(list[y]) and list[y][x+1] == list[y][x] +1:
        l.extend(findnumtrails(list, y, x+1))
    if x-1 >= 0 and list[y][x-1] == list[y][x] +1:
        l.extend(findnumtrails(list, y, x-1))
    if y+1 < len(list) and list[y+1][x] == list[y][x] +1:
        l.extend(findnumtrails(list, y+1, x))
    if y-1 >= 0 and list[y-1][x] == list[y][x] +1:
        l.extend(findnumtrails(list, y-1, x))
    return l

def sumup(list :list) -> int:
    sum = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 0:
                l = findnumtrails(list, i, j)
                r = []
                for element in l:
                    if element not in r:
                        r.append(element)
                sum += len(r)
    return sum

def findnumtrailsp2(list :list, y :int, x :int) -> int:
    if list[y][x] == 9:
        return 1
    num = 0
    if x+1 < len(list[y]) and list[y][x+1] == list[y][x] +1:
        num += findnumtrailsp2(list, y, x+1)
    if x-1 >= 0 and list[y][x-1] == list[y][x] +1:
        num += findnumtrailsp2(list, y, x-1)
    if y+1 < len(list) and list[y+1][x] == list[y][x] +1:
        num += findnumtrailsp2(list, y+1, x)
    if y-1 >= 0 and list[y-1][x] == list[y][x] +1:
        num += findnumtrailsp2(list, y-1, x)
    return num

def sumupp2(list :list) -> int:
    sum = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 0:
                sum += findnumtrailsp2(list, i, j)
    return sum


def part1():
    input = puzzleinput
    hike = []
    for line in input.split('\n'):
        tmp = []
        for char in line:
            tmp.append(int(char))
        hike.append(tmp)
    print(sumup(hike))

def part2():
    input = puzzleinput
    hike = []
    for line in input.split('\n'):
        tmp = []
        for char in line:
            tmp.append(int(char))
        hike.append(tmp)
    print(sumupp2(hike))
    print()

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")