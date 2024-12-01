puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day3/day3.txt', 'r') as file:
    puzzleinput = file.read()

def part1():
    map = [[[0, 0], 1]]

    currentvector = [0, 0]
    
    for char in puzzleinput:
        match char:
            case '^':
                currentvector[0] += 1
            case '>':
                currentvector[1] += 1
            case '<':
                currentvector[1] += -1
            case 'v':
                currentvector[0] += -1

        foundcase = False

        for mapcase in map:
            if mapcase[0] == currentvector:
                mapcase[1] += 1
                foundcase = True
                break
        if foundcase == False:
            map.append([currentvector.copy(), 1])

    print(f"Santa found a total of {len(map)} houses.")

def part2():
    map = [[[0, 0], 1]]

    currentvectorsanta = [0, 0]
    currentvectorrobot = [0, 0]

    santasturn = True
    
    for char in puzzleinput:
        match char:
            case '^':
                if santasturn:
                    currentvectorsanta[0] += 1
                else:
                    currentvectorrobot[0] += 1
            case '>':
                if santasturn:
                    currentvectorsanta[1] += 1
                else:
                    currentvectorrobot[1] += 1
            case '<':
                if santasturn:
                    currentvectorsanta[1] += -1
                else:
                    currentvectorrobot[1] += -1
            case 'v':
                if santasturn:
                    currentvectorsanta[0] += -1
                else:
                    currentvectorrobot[0] += -1

        foundcase = False
        if santasturn:
            for mapcase in map:
                if mapcase[0] == currentvectorsanta:
                    mapcase[1] += 1
                    foundcase = True
                    break
            if foundcase == False:
                map.append([currentvectorsanta.copy(), 1])
        else:
            for mapcase in map:
                if mapcase[0] == currentvectorrobot:
                    mapcase[1] += 1
                    foundcase = True
                    break
            if foundcase == False:
                map.append([currentvectorrobot.copy(), 1])

        santasturn = not santasturn

    print(f"Santa and his Robot found a total of {len(map)} houses.")

part1()
part2()