puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day8/day8.txt', 'r') as file:
    puzzleinput = file.read()

testinput = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def makefrequencieoverlaps(frequencylist :list, overlaplist :list, part2 :bool):
    for i in range(len(frequencylist)):
        for j in range(len(frequencylist[i])):
            if frequencylist[i][j] != '.':
                for y in range(len(frequencylist)):
                    for x in range(len(frequencylist[y])):
                        if frequencylist[i][j] == frequencylist[y][x]:
                            deltax = j - x
                            deltay = i - y

                            if deltax == 0 and deltay == 0:
                                continue

                            if part2:
                                curx = j
                                cury = i
                                while cury + deltay >= 0 and cury + deltay < len(frequencylist) and curx + deltax >= 0 and curx + deltax < len(frequencylist[cury + deltay]):
                                    cury += deltay
                                    curx += deltax
                                string = overlaplist[cury][:curx] + '#' + overlaplist[cury][curx +1:]
                                overlaplist[cury] = string
                                while cury - deltay >= 0 and cury - deltay < len(frequencylist) and curx - deltax >= 0 and curx - deltax < len(frequencylist[cury - deltay]):
                                    cury -= deltay
                                    curx -= deltax
                                    string = overlaplist[cury][:curx] + '#' + overlaplist[cury][curx +1:]
                                    overlaplist[cury] = string
                                
                            else:
                                if i + deltay == y + deltay + deltay and j + deltax == x + deltax + deltax and i + deltay < len(overlaplist) and j + deltax < len(overlaplist[i+deltay]) and i + deltay >= 0 and j + deltax >= 0:
                                    string = overlaplist[i+deltay][:j+deltax] + '#' + overlaplist[i+deltay][j+deltax +1:]
                                    overlaplist[i+deltay] = string

                                elif i - deltay == y - deltay - deltay and j - deltax == x - deltax - deltax and i - deltay < len(overlaplist) and j - deltax < len(overlaplist[i-deltay]) and i - deltay >= 0 and j - deltax >= 0:
                                    string = overlaplist[i-deltay][:j-deltax] + '#' + overlaplist[i-deltay][j-deltax +1:]
                                    overlaplist[i-deltay] = string

                                if y + deltay == i + deltay + deltay and x + deltax == j + deltax + deltax and y + deltay < len(overlaplist) and x + deltax < len(overlaplist[y+deltay]) and y + deltay >= 0 and x + deltax >= 0:
                                    string = overlaplist[y+deltay][:x+deltax] + '#' + overlaplist[y+deltay][x+deltax +1:]
                                    overlaplist[y+deltay] = string

                                elif y - deltay == i - deltay - deltay and x - deltax == j - deltax - deltax and y - deltay < len(overlaplist) and x - deltax < len(overlaplist[y-deltay]) and y - deltay >= 0 and x - deltax >= 0:
                                    string = overlaplist[y-deltay][:x-deltax] + '#' + overlaplist[y-deltay][x-deltax +1:]
                                    overlaplist[y-deltay] = string




def countlocations(list :list) -> int:
    count = 0
    for line in list:
        for char in line:
            if char == '#':
                count += 1
    return count

def part1():
    input = puzzleinput
    frequencylist = []
    for line in input.split('\n'):
        frequencylist.append(line)
    overlaplist = []
    for line in frequencylist:
        string = ''
        for i in range(len(line)):
            string += '.'
        overlaplist.append(string)
    makefrequencieoverlaps(frequencylist, overlaplist, False)
    print(countlocations(overlaplist))

def part2():
    input = puzzleinput
    frequencylist = []
    for line in input.split('\n'):
        frequencylist.append(line)
    overlaplist = []
    for line in frequencylist:
        string = ''
        for i in range(len(line)):
            string += '.'
        overlaplist.append(string)
    makefrequencieoverlaps(frequencylist, overlaplist, True)
    print(countlocations(overlaplist))
    print()

part1()
part2()