puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day12/day12.txt', 'r') as file:
    puzzleinput = file.read()

done = []

testinput = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

def getperimeter(list :list, i :int, j :int, peri :list = None) -> int:
    if peri == None:
        peri = []
    peri.append([i, j])
    perimeter = 0
    if j < len(list[i]) -1 and (not ([i, j+1] in peri)) and list[i][j+1] == list[i][j]:
        perimeter += getperimeter(list, i, j+1, peri)
    if j > 0 and (not ([i, j-1] in peri)) and list[i][j-1] == list[i][j]:
        perimeter += getperimeter(list, i, j-1, peri)
    if i < len(list) -1 and (not ([i+1, j] in peri)) and list[i+1][j] == list[i][j]:
        perimeter += getperimeter(list, i+1, j, peri)
    if i > 0 and (not ([i-1, j] in peri)) and list[i-1][j] == list[i][j]:
        perimeter += getperimeter(list, i-1, j, peri)

    if j < len(list[i]) -1 and list[i][j+1] != list[i][j]:
        perimeter += 1
    if j > 0 and list[i][j-1] != list[i][j]:
        perimeter += 1
    if i < len(list) -1 and list[i+1][j] != list[i][j]:
        perimeter += 1
    if i > 0 and list[i-1][j] != list[i][j]:
        perimeter += 1
    
    if j == len(list[i]) -1:
        perimeter += 1
    if j == 0:
        perimeter += 1
    if i == len(list) -1:
        perimeter += 1
    if i == 0:
        perimeter += 1

    return perimeter

def getarea(list :list, i :int, j :int) -> int:
    area = 1
    global done
    done.append([i, j])
    if j < len(list[i]) -1 and (not ([i, j+1] in done)) and list[i][j+1] == list[i][j]:
        area += getarea(list, i, j+1)
    if j > 0 and (not ([i, j-1] in done)) and list[i][j-1] == list[i][j]:
        area += getarea(list, i, j-1)
    if i < len(list) -1 and (not ([i+1, j] in done)) and list[i+1][j] == list[i][j]:
        area += getarea(list, i+1, j)
    if i > 0 and (not ([i-1, j] in done)) and list[i-1][j] == list[i][j]:
        area += getarea(list, i-1, j)
    return area

# TODO: pls fix
def getsides(list :list, i :int, j :int, sides :list = None) -> int:
    side = 0
    if sides == None:
        sides = []
    sides.append([i, j])

    if j < len(list[i]) -1 and list[i][j+1] != list[i][j]:
        side += 1
    if j > 0 and list[i][j-1] != list[i][j]:
        side += 1
    if i < len(list) -1 and list[i+1][j] != list[i][j]:
        side += 1
    if i > 0 and list[i-1][j] != list[i][j]:
        side += 1
    
    if j == len(list[i]) -1:
        side += 1
    if j == 0:
        side += 1
    if i == len(list) -1:
        side += 1
    if i == 0:
        side += 1
    return side

def part1():
    global done
    done = []
    input = testinput
    list = []
    price = 0
    for line in input.split('\n'):
        list.append(line)
    for i in range(len(list)):
        for j in range(len(list[i])):
            if not ([i, j] in done):
                perimeter = getperimeter(list, i, j)
                area = getarea(list, i , j)
                price += perimeter * area

    print(price)

def part2():
    global done
    done = []
    input = testinput
    list = []
    price = 0
    for line in input.split('\n'):
        list.append(line)
    for i in range(len(list)):
        for j in range(len(list[i])):
            if not ([i, j] in done):
                sides = getsides(list, i, j)
                area = getarea(list, i , j)
                print(f'{area} * {sides}')
                price += sides * area

    print(price)

part1()
part2()