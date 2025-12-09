puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day5/day5.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

def part1():
    naughtybits = ["ab", "cd", "pq", "xy"]

    nicestringcount = 0

    for line in puzzleinput.split('\n'):
        vowelcount = 0
        doubleletter = False

        naughty = False
        for naughtybit in naughtybits:
            if naughtybit in line:
                print("naughty bit in the line")
                naughty = True
                break
        if naughty:
            continue

        lastchar = ''
        for char in line:
            if char == lastchar:
                doubleletter = True
            match char:
                case 'a':
                    vowelcount += 1
                case 'e':
                    vowelcount += 1
                case 'i':
                    vowelcount += 1
                case 'o':
                    vowelcount += 1
                case 'u':
                    vowelcount += 1
            lastchar = char
        if vowelcount < 3:
            print("vowels less than 3")
            continue
        if not doubleletter:
            print("no doubleletter")
            continue
        nicestringcount += 1
    
    print(f"The amount of nice string is {nicestringcount}")

def part2():
    nicestringcount = 0

    for line in puzzleinput.split('\n'):
        doubled = False
        tripled = False
        sequenceof2chars = ''
        sequenceof3chars = ''
        for char in line:
            if len(sequenceof2chars) < 2:
                sequenceof2chars += char
            else:
                sequenceof2chars = sequenceof2chars[1] + char
            if len(sequenceof3chars) < 3:
                sequenceof3chars += char
            else:
                sequenceof3chars = sequenceof3chars[1] + sequenceof3chars[2] + char
            if len(sequenceof2chars) < 2:
                continue

            if line.count(sequenceof2chars) >= 2:
                doubled = True

            if len(sequenceof3chars) < 3:
                continue

            if sequenceof3chars[0] == sequenceof3chars[2]:
                tripled = True

        if doubled and tripled:
            nicestringcount += 1
        
    
    print(f"The amount of nice string is {nicestringcount}")

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")