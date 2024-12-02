puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day6/day6.txt', 'r') as file:
    puzzleinput = file.read()

def initarray():
    array = []
    for i in range(0, 1000):
        tmparray = []
        for j in range(0, 1000):
            tmparray.append(False)
        array.append(tmparray.copy())
    return array

def initarrayint():
    array = []
    for i in range(0, 1000):
        tmparray = []
        for j in range(0, 1000):
            tmparray.append(0)
        array.append(tmparray.copy())
    return array

def part1():
    startingarray = initarray()
    for line in puzzleinput.split('\n'):
        mode = 1                                #turn on will be 1, toggle 0, turn off -1
        if line.startswith("turn on "):
            mode = 1
            line = line.split("turn on ")[1]
        if line.startswith("toggle "):
            mode = 0
            line = line.split("toggle ")[1]
        if line.startswith("turn off "):
            mode = -1
            line = line.split("turn off ")[1]
        line = line.split("through ")[0] + line.split("through ")[1]
        line = line.replace(',', ' ') # now a line should only be like "1 2 3 4"
        numchars = line.split(' ')
        startx = int(numchars[0])
        starty = int(numchars[1])
        endx = int(numchars[2])
        endy = int(numchars[3])

        for i in range(startx, endx + 1):
            for j in range(starty, endy + 1):
                if mode == 1:
                    startingarray[i][j] = True
                elif mode == 0:
                    startingarray[i][j] = not startingarray[i][j]
                elif mode == -1:
                    startingarray[i][j] = False
    counter = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if startingarray[i][j] == True:
                counter += 1
    print(f"the total amount of lit lights is {counter}")

def part2():
    startingarray = initarrayint()
    for line in puzzleinput.split('\n'):
        mode = 1                                #turn on will be 1, toggle 0, turn off -1
        if line.startswith("turn on "):
            mode = 1
            line = line.split("turn on ")[1]
        if line.startswith("toggle "):
            mode = 0
            line = line.split("toggle ")[1]
        if line.startswith("turn off "):
            mode = -1
            line = line.split("turn off ")[1]
        line = line.split("through ")[0] + line.split("through ")[1]
        line = line.replace(',', ' ') # now a line should only be like "1 2 3 4"
        numchars = line.split(' ')
        startx = int(numchars[0])
        starty = int(numchars[1])
        endx = int(numchars[2])
        endy = int(numchars[3])

        for i in range(startx, endx + 1):
            for j in range(starty, endy + 1):
                if mode == 1:
                    startingarray[i][j] += 1
                elif mode == 0:
                    startingarray[i][j] += 2
                elif mode == -1:
                    startingarray[i][j] += -1
                    if startingarray[i][j] < 0:
                        startingarray[i][j] = 0
    totalbrightness = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            totalbrightness += startingarray[i][j]
    print(f"the total brightness of the lights is {totalbrightness}")

part1()
part2()