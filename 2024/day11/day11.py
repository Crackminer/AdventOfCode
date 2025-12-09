import functools
from datetime import datetime

puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day11/day11.txt', 'r') as file:
    puzzleinput = file.read()

testinput = "125 17"

def blink(list :list) -> list:
    newlist = []
    for element in list:
        num = getnum(element)
        if type(num) is int:
            newlist.append(num)
        else:
            newlist.append(num[0])
            newlist.append(num[1])
    return newlist

@functools.cache
def getnum(num :int) -> int | tuple:
    if num == 0:
        return 1
    elif len(str(num)) % 2 == 0:
        string = str(num)
        return int(string[:int(len(string) / 2)]), int(string[int(len(string) / 2):])
    else:
        return num * 2024
    
# thanks to thomasjevskij, because i would not have gotten this myself at all. My former brute force method went out of ram and stopped to process after hitting about 58GB of ram for like the 10th time. https://github.com/thomasjevskij/advent_of_code/blob/master/2024/aoc11/day11.py
@functools.cache
def blinkp2(number):
    if number == 0:
        return [1]
    s = f'{number}'
    l = len(s)
    if l % 2 == 0:
        return [int(n) for n in [s[:l//2], s[l//2:]]]
    return [number * 2024]

@functools.cache
def countsplits(number, blinks):
    if blinks == 0:
        return 1
    return sum(countsplits(num, blinks -1) for num in blinkp2(number))

def part1():
    input = puzzleinput
    list = []
    for numstring in input.split(' '):
        list.append(int(numstring))
    for i in range(25):
        list = blink(list)
    print(len(list))

def part2():
    input = puzzleinput
    list = []
    for numstring in input.split(' '):
        list.append(int(numstring))
    print(sum(countsplits(num, 75) for num in list))

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")