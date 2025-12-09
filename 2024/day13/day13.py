puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day13/day13.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

testinput = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

def comparenotbelowzero(list :list) -> bool:
    for element in list:
        if element < 0:
            return False
    return True

def subtractlist(list :list, list2 :list) -> list:
    returnlist = []
    for i in range(len(list)):
        returnlist.append(list[i] - list2[i])
    return returnlist

def getsum(block :list, a :int = 0, b :int = 0) -> int:
    suma = 0
    sumb = 0
    if a != 100 and comparenotbelowzero(subtractlist(block[2], block[0])):
        newblock = block.copy()
        newblock[2] = subtractlist(newblock[2], newblock[0])
        suma = getsum(newblock, a+1, b)
    if b != 100 and comparenotbelowzero(subtractlist(block[2], block[1])):
        newblock = block.copy()
        newblock[2] = subtractlist(newblock[2], newblock[1])
        sumb = getsum(newblock, a, b+1)
    if suma < sumb:
        return suma
    return sumb

def part1():
    input = testinput
    blocks = []
    for blockstr in input.split('\n\n'):
        block = []
        for line in blockstr.split('\n'):
            if line.startswith('Button'):
                button = []
                splitted = line.split(' ')
                button.append(int(splitted[2][2:-1]))
                button.append(int(splitted[3][2:]))
                block.append(button)
            elif line.startswith('Prize'):
                prize = []
                splitted = line.split(' ')
                prize.append(int(splitted[1][2:-1]))
                prize.append(int(splitted[2][2:]))
                block.append(prize)
        blocks.append(block)
    sum = 0
    for block in blocks:
        sum += getsum(block)
        print('got a new total sum: ' + str(sum))
    print(sum)

def part2():
    print()

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")