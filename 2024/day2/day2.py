puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day2/day2.txt', 'r') as file:
    puzzleinput = file.read()

def checksafe(line : str) -> bool:
    previous = 50000000
    descendingcount = 0
    ascendingcount = 0
    for numchar in line.split(' '):
        if previous == 50000000:
            previous = int(numchar)
            continue
        if previous < int(numchar):
            ascendingcount += 1
        elif previous > int(numchar):
            descendingcount += 1
        
        tmp = previous - int(numchar)
        if tmp < 0:
            tmp *= -1
        
        if tmp > 3:
            return False
        previous = int(numchar)
    
    if descendingcount == len(line.split(' ')) -1:
        return True
    if ascendingcount == len(line.split(' ')) -1:
        return True
    return False

def part1():
    safecount = 0
    for line in puzzleinput.split('\n'):
        if checksafe(line):
            safecount += 1
            
    print(f'There is a total of {safecount} safe lines.')

def part2():
    safecount = 0
    for line in puzzleinput.split('\n'):
        numchars = line.split(' ')
        for i in range(0, len(numchars)):
            linemock = ""
            counter = 0
            for numchar in numchars:
                if counter != i:
                    linemock += numchar
                    linemock += " "
                counter += 1
            linemock = linemock.removesuffix(" ")
            if checksafe(linemock):
                safecount += 1
                break
            
    print(f'There is a total of {safecount} safe lines.')

part1()
part2()