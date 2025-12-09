import json
from datetime import datetime

puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day12/day12.txt', 'r') as file:
    puzzleinput = file.read()

def recursivedictsearchfornums(data :dict) -> int:
    sum = 0
    for key, value in data.items():
        if type(value) == int:
            sum += value
        elif type(value) == list:
            sum += recursivelistsearchfornums(value)
        elif type(value) == dict:
            sum += recursivedictsearchfornums(value)
        elif type(value) == str:
            continue
    return sum


def recursivelistsearchfornums(data :list) -> int:
    sum = 0
    for object in data:
        if type(object) == int:
            sum += object
        elif type(object) == list:
            sum += recursivelistsearchfornums(object)
        elif type(object) == dict:
            sum += recursivedictsearchfornums(object)
        elif type(object) == str:
            continue
    return sum

def recursivedictsearchfornumsignorered(data :dict) -> int:
    sum = 0
    for key, value in data.items():
        if type(value) == int:
            sum += value
        elif type(value) == list:
            sum += recursivelistsearchfornumsignorered(value)
        elif type(value) == dict:
            sum += recursivedictsearchfornumsignorered(value)
        elif type(value) == str:
            if value == "red":
                return 0
            continue
    return sum


def recursivelistsearchfornumsignorered(data :list) -> int:
    sum = 0
    for object in data:
        if type(object) == int:
            sum += object
        elif type(object) == list:
            sum += recursivelistsearchfornumsignorered(object)
        elif type(object) == dict:
            sum += recursivedictsearchfornumsignorered(object)
        elif type(object) == str:
            continue
    return sum

def part1():
    file = open('2015/day12/day12.txt', 'r+')
    data = json.load(file)
    sum = 0
    if type(data) == list:  #it starts as an array
        sum += recursivelistsearchfornums(data)
    file.close()
    print(sum)

def part2():
    file = open('2015/day12/day12.txt', 'r+')
    data = json.load(file)
    sum = 0
    if type(data) == list:  #it starts as an array
        sum += recursivelistsearchfornumsignorered(data)
    file.close()
    print(sum)

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")