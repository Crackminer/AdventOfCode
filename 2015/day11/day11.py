puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day11/day11.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

#puzzleinput = "aabbbz"

def invalid(pw :str) -> bool:
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return True
    pre1 = ''
    pre2 = ''
    doubles = 0
    ascending = False
    doubled = []
    for char in pw:
        if pre2 == char and pre1 != pre2 and char not in doubled:
            doubles += 1
            doubled.append(char)
        
        if pre1 != '' and ord(pre1) +1 == ord(pre2) and ord(pre2) +1 == ord(char):
            ascending = True
        
        pre1 = pre2
        pre2 = char
    
    if doubles < 2:
        return True    

    return not ascending

def increment(char :str):
    if char == 'z':
        return 'a', True
    return chr(ord(char) +1), False

def tostring(list :list) -> str:
    string = ""
    for char in list:
        string += char
    return string

def getvalidline(line :str) -> str:
    while invalid(line):
        i = len(line) -1
        carryover = True
        linelist = list(line)
        while carryover:
            linelist[i], carryover = increment(line[i])
            i -= 1
        line = tostring(linelist)
    return line


def part1():
    print(getvalidline(puzzleinput))

def part2():
    line = getvalidline(puzzleinput)
    listline = list(line)
    i = len(listline) -1
    carryover = True
    while carryover:
        listline[i], carryover = increment(listline[i])
        i -= 1
    line = tostring(listline)
    print(getvalidline(line))

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")