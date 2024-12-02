puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day10/day10.txt', 'r') as file:
    puzzleinput = file.read()

#puzzleinput = '1'

def part1():
    line = puzzleinput
    for i in range(0, 40):
        newline = ""
        prevchar = ''
        curcharcount = 0
        counter = 0
        for char in line:
            counter += 1
            if prevchar == '':
                prevchar = char
            elif prevchar != char:
                newline += f'{curcharcount}{prevchar}'
                curcharcount = 0
                prevchar = char
            curcharcount += 1
            if counter == len(line):
                newline += f'{curcharcount}{prevchar}'
        line = newline


    print(len(line))

def part2():
    line = puzzleinput
    for i in range(0, 50):
        newline = ""
        prevchar = ''
        curcharcount = 0
        counter = 0
        for char in line:
            counter += 1
            if prevchar == '':
                prevchar = char
            elif prevchar != char:
                newline += f'{curcharcount}{prevchar}'
                curcharcount = 0
                prevchar = char
            curcharcount += 1
            if counter == len(line):
                newline += f'{curcharcount}{prevchar}'
        line = newline
    print(len(line))

part1()
part2()