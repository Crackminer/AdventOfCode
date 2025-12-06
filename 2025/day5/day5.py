puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2025/day5/day5.txt', 'r') as file:
    puzzleinput = file.read()

testinput = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""



def part1():
    #puzzleinput = testinput
    ranges = []
    singles = []
    single = False
    for line in puzzleinput.splitlines():
        if line == '':
            single = True
            continue
        if single:
            singles.append(int(line))
        else:
            ranges.append((int(line.split('-')[0]), int(line.split('-')[1])))

    freshcount = 0

    for ingredient in singles:
        for num1, num2 in ranges:
            if ingredient >= num1 and ingredient <= num2:
                freshcount += 1
                break


    print(freshcount)

def part2():
    #puzzleinput = testinput
    ranges = []
    for line in puzzleinput.splitlines():
        if line == '':
            break
        ranges.append((int(line.split('-')[0]), int(line.split('-')[1])))

    ranges.sort()

    # für alle elemente im SORTIERTEN ranges schaue nach ob die ranges sich überschneiden und ziehe die ranges dementsprechend hoch
    # Dieser Schritt ist hoch wichtig um massiv Rechenaufwand zu sparen. Meine vorherige Lösung war ein durchgehen 'for i in range(num1, num2+1)' 
    # was absolut uncool für Memory ist -> hatte MemoryError weil ich alle i in einem set unter gebracht hatte um doppelte i rauszufiltern. 
    # Klappt super für den kleinen Testinput, ist aber absolut nicht ausreichend für den puzzleinput
    index = 0
    while index < len(ranges)-1:
        range1 = ranges[index]
        range2 = ranges[index+1]
        # wenn die range2 innerhalb der range1 anfängt (es muss nicht nach range1[0] geschaut werden, da sort das bereits übernommen hat, heißt es geht nur nach range[0] und sortiert dann von klein nach groß -> range1[0] ist immer kleiner als range2[0])
        if range1[1] >= range2[0]:
            # Aufpassen, manchmal umschließt die erste Range die 2. Range vollständig!
            newRange = (range1[0], (range2[1] if range2[1] >= range1[1] else range1[1]))
            # eigentliche range wird angepasst
            ranges[index] = newRange
            # die eingeschlossene range wird gelöscht, wir benötigen sie nicht mehr
            ranges.pop(index+1)
        else:
            index += 1

    freshcount = 0

    for num1, num2 in ranges:
        freshcount += num2 - num1 +1
    
    print(freshcount)


part1()
part2()