puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day9/day9.txt', 'r') as file:
    puzzleinput = file.read()

#puzzleinput = '''London to Dublin = 464
#London to Belfast = 518
#Dublin to Belfast = 141'''

def findinmap(mapp :list, source :str, dest :str) -> int:
    for trip in mapp:
        if trip[0] == source and trip[1] == dest:
            return trip[2]

def recursivefuncshortest(mapp :list, tovisit :list, imat :str) -> int:
    if tovisit == []:
        return 0
    trip = 5000000
    for i in range(0, len(tovisit)):
        copyarr = tovisit.copy()
        dest = copyarr.pop(i)
        route = findinmap(mapp, imat, dest)
        tmp =  route + recursivefuncshortest(mapp, copyarr, dest)
        if tmp < trip:
            trip = tmp
    return trip

def recursivefunclongest(mapp :list, tovisit :list, imat :str) -> int:
    if tovisit == []:
        return 0
    trip = 0
    for i in range(0, len(tovisit)):
        copyarr = tovisit.copy()
        dest = copyarr.pop(i)
        route = findinmap(mapp, imat, dest)
        tmp =  route + recursivefunclongest(mapp, copyarr, dest)
        if tmp > trip:
            trip = tmp
    return trip

def part1():
    mapp = []
    for line in puzzleinput.split('\n'):
        length = int(line.split(' = ')[1])
        source, dest = line.split(' = ')[0].split(' to ')
        mapp.append([source, dest, length])
        mapp.append([dest, source, length])
    print(mapp)
    tovisit = []
    for route in mapp:
        if route[0] not in tovisit:
            tovisit.append(route[0])
    shortesttrip = 5000000
    for string in tovisit:
        copyarr = tovisit.copy()
        copyarr.remove(string)
        integer = recursivefuncshortest(mapp, copyarr, string)
        if integer < shortesttrip:
            shortesttrip = integer
        
    print(shortesttrip)

def part2():
    mapp = []
    for line in puzzleinput.split('\n'):
        length = int(line.split(' = ')[1])
        source, dest = line.split(' = ')[0].split(' to ')
        mapp.append([source, dest, length])
        mapp.append([dest, source, length])
    print(mapp)
    tovisit = []
    for route in mapp:
        if route[0] not in tovisit:
            tovisit.append(route[0])
    longesttrip = 0
    for string in tovisit:
        copyarr = tovisit.copy()
        copyarr.remove(string)
        integer = recursivefunclongest(mapp, copyarr, string)
        if integer > longesttrip:
            longesttrip = integer
        
    print(longesttrip)

part1()
part2()