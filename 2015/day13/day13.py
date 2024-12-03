from itertools import permutations

puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day13/day13.txt', 'r') as file:
    puzzleinput = file.read()

def getlikelist(input :str) -> list:
    likelist = []
    for line in input.split('\n'):
        linelist = line.split(' ')
        source = linelist[0]
        destination = linelist[-1].removesuffix('.')
        happiness = int(linelist[3])
        positive = linelist[2] == "gain"
        if not positive:
            happiness *= -1
        likelist.append([source, destination, happiness])
    return likelist

def getlike(list :list, source :str, dest: str) -> int:
    for item in list:
        if item[0] == source and item[1] == dest:
            return item[2]
    return 0

def part1():
    likelist = getlikelist(puzzleinput)
    totalhappiness = 0
    allpeople = []
    for item in likelist:
        if item[0] not in allpeople:
            allpeople.append(item[0])
    configs = permutations(allpeople)
        
    
    for tableconfig in configs:
        happiness = 0
        for i in range(0, len(tableconfig)):
            happiness += getlike(likelist, tableconfig[i], tableconfig[i-1])
            happiness += getlike(likelist, tableconfig[i-1], tableconfig[i])
        if happiness > totalhappiness:
            totalhappiness = happiness
            

    print(totalhappiness)

def part2():
    likelist = getlikelist(puzzleinput)
    totalhappiness = 0
    allpeople = []
    for item in likelist:
        if item[0] not in allpeople:
            allpeople.append(item[0])
    allpeople.append('me')
    configs = permutations(allpeople)
        
    
    for tableconfig in configs:
        happiness = 0
        for i in range(0, len(tableconfig)):
            happiness += getlike(likelist, tableconfig[i], tableconfig[i-1])
            happiness += getlike(likelist, tableconfig[i-1], tableconfig[i])
        if happiness > totalhappiness:
            totalhappiness = happiness
            

    print(totalhappiness)

part1()
part2()