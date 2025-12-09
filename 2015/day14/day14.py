puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day14/day14.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

def getproperlist(input :str) -> list:
    list = []
    for line in input.split('\n'):
        strings = line.split(' ')
        reindeer = strings[0]
        speed = int(strings[3])
        maxstamina = int(strings[6])
        restingtime = int(strings[13])
        #name, speed stamina, resttime, distance, usedstamina, usedrestingtime, totalpoints
        #                0       1        2             3      4  5  6  7
        list.append([reindeer, speed, maxstamina, restingtime, 0, 0, 0, 0])
    return list

def part1():
    list = getproperlist(puzzleinput)
    for i in range(0, 2503):
        for item in list:
            #resting, used stamina is max stamina
            if item[2] == item[5]:
                #usedrestingtime ++
                item[6] += 1
                # resting has now finished, resume at next second
                if item[6] == item[3]:
                    # restingtime reset
                    item[6] = 0
                    # usedstamina reset
                    item[5] = 0
            #if not resting means racing
            else:
                # usedstamina ++
                item[5] += 1
                # travlelled distance += speed
                item[4] += item[1]
    mostdistance = 0
    for item in list:
        if item[4] > mostdistance:
            mostdistance = item[4]
    print(mostdistance)

def part2():
    list = getproperlist(puzzleinput)
    for i in range(0, 2503):
        for item in list:
            #resting, used stamina is max stamina
            if item[2] == item[5]:
                #usedrestingtime ++
                item[6] += 1
                # resting has now finished, resume at next second
                if item[6] == item[3]:
                    # restingtime reset
                    item[6] = 0
                    # usedstamina reset
                    item[5] = 0
            #if not resting means racing
            else:
                # usedstamina ++
                item[5] += 1
                # travlelled distance += speed
                item[4] += item[1]
        mostdistance = 0
        for item in list:
            if item[4] > mostdistance:
                mostdistance = item[4]
        for item in list:
            if item[4] == mostdistance:
                item[7] += 1
    mostpoints = 0
    for item in list:
        if item[7] > mostpoints:
            mostpoints = item[7]
    print(mostpoints)

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")