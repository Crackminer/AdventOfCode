puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day21/day21.txt', 'r') as file:
    puzzleinput = file.read()
#       HP, ATK, DEF
player = [100, 0, 0]

weaponshop = [['Dagger', 8, 4, 0], ['Shortsword', 10, 5, 0], ['Warhammer', 25, 6, 0], ['Longsword', 40, 7, 0], ['Greataxe', 74, 8, 0]]

armorshop = [['Leather', 13, 0, 1], ['Chainmail', 31, 0, 2], ['Splintmail', 53, 0, 3], ['Bandedmail', 75, 0, 4], ['Platemail', 102, 0, 5]]

ringshop = [['Damage +1', 25, 1, 0], ['Damage +2', 50, 2, 0], ['Damage +3', 100, 3, 0], ['Defense +1', 20, 0, 1], ['Defense +2', 40, 0, 2], ['Defense +3', 80, 0, 3]]

def notdead(entity :list) -> bool:
    return entity[0] > 0

def simulateattacktillonedead(player :list, enemy :list) -> bool:
    while notdead(player) and notdead(enemy):
        enemy[0] -= max(player[1] - enemy[2], 1)
        if not notdead(enemy):
            return True
        player[0] -= max(enemy[1] - player[2], 1)
    return False

def part1():
    enemy = []
    for line in puzzleinput.split('\n'):
        string = line.split(' ')[1]
        enemy.append(int(string))
    lowestcost = 50000
    for i in range(3):
        for j in range(2):
            for weapon in weaponshop:
                if j == 1:
                    for armor in armorshop:
                        if i == 1:
                            for ring in ringshop:
                                playercopy = player.copy()
                                playercopy[1] += ring[2]
                                playercopy[2] += ring[3]
                                playercopy[2] += armor[3]
                                playercopy[1] += weapon[2]
                                cost = ring[1] + armor[1] + weapon[1]
                                enemycopy = enemy.copy()
                                if simulateattacktillonedead(playercopy, enemycopy):
                                    if cost < lowestcost:
                                        lowestcost = cost
                        elif i == 2:
                            for ring in ringshop:
                                ringshopcopy = ringshop.copy()
                                tocastintothefire = ring
                                ringshopcopy.remove(tocastintothefire)
                                for ring2 in ringshopcopy: 
                                    playercopy = player.copy()
                                    playercopy[1] += ring[2]
                                    playercopy[2] += ring[3]
                                    playercopy[1] += ring2[2]
                                    playercopy[2] += ring2[3]
                                    playercopy[2] += armor[3]
                                    playercopy[1] += weapon[2]
                                    cost = ring[1] + ring2[1] + armor[1] + weapon[1]
                                    enemycopy = enemy.copy()
                                    if simulateattacktillonedead(playercopy, enemycopy):
                                        if cost < lowestcost:
                                            lowestcost = cost
                        else:
                            playercopy = player.copy()
                            playercopy[2] += armor[3]
                            playercopy[1] += weapon[2]
                            cost = armor[1] + weapon[1]
                            enemycopy = enemy.copy()
                            if simulateattacktillonedead(playercopy, enemycopy):
                                if cost < lowestcost:
                                    lowestcost = cost
                else:
                    if i == 1:
                        for ring in ringshop:
                            playercopy = player.copy()
                            playercopy[1] += ring[2]
                            playercopy[2] += ring[3]
                            playercopy[1] += weapon[2]
                            cost = ring[1] + weapon[1]
                            enemycopy = enemy.copy()
                            if simulateattacktillonedead(playercopy, enemycopy):
                                if cost < lowestcost:
                                    lowestcost = cost
                    elif i == 2:
                        for ring in ringshop:
                            ringshopcopy = ringshop.copy()
                            tocastintothefire = ring
                            ringshopcopy.remove(tocastintothefire)
                            for ring2 in ringshopcopy: 
                                playercopy = player.copy()
                                playercopy[1] += ring[2]
                                playercopy[2] += ring[3]
                                playercopy[1] += ring2[2]
                                playercopy[2] += ring2[3]
                                playercopy[1] += weapon[2]
                                cost = ring[1] + ring2[1] + weapon[1]
                                enemycopy = enemy.copy()
                                if simulateattacktillonedead(playercopy, enemycopy):
                                    if cost < lowestcost:
                                        lowestcost = cost
                    else:
                        playercopy = player.copy()
                        playercopy[1] += weapon[2]
                        cost = weapon[1]
                        enemycopy = enemy.copy()
                        if simulateattacktillonedead(playercopy, enemycopy):
                            if cost < lowestcost:
                                lowestcost = cost

    print(lowestcost)

def part2():
    enemy = []
    for line in puzzleinput.split('\n'):
        string = line.split(' ')[1]
        enemy.append(int(string))
    highestcost = 0
    for i in range(3):
        for j in range(2):
            for weapon in weaponshop:
                if j == 1:
                    for armor in armorshop:
                        if i == 1:
                            for ring in ringshop:
                                playercopy = player.copy()
                                playercopy[1] += ring[2]
                                playercopy[2] += ring[3]
                                playercopy[2] += armor[3]
                                playercopy[1] += weapon[2]
                                cost = ring[1] + armor[1] + weapon[1]
                                enemycopy = enemy.copy()
                                if not simulateattacktillonedead(playercopy, enemycopy):
                                    if cost > highestcost:
                                        highestcost = cost
                        elif i == 2:
                            for ring in ringshop:
                                ringshopcopy = ringshop.copy()
                                tocastintothefire = ring
                                ringshopcopy.remove(tocastintothefire)
                                for ring2 in ringshopcopy: 
                                    playercopy = player.copy()
                                    playercopy[1] += ring[2]
                                    playercopy[2] += ring[3]
                                    playercopy[1] += ring2[2]
                                    playercopy[2] += ring2[3]
                                    playercopy[2] += armor[3]
                                    playercopy[1] += weapon[2]
                                    cost = ring[1] + ring2[1] + armor[1] + weapon[1]
                                    enemycopy = enemy.copy()
                                    if not simulateattacktillonedead(playercopy, enemycopy):
                                        if cost > highestcost:
                                            highestcost = cost
                        else:
                            playercopy = player.copy()
                            playercopy[2] += armor[3]
                            playercopy[1] += weapon[2]
                            cost = armor[1] + weapon[1]
                            enemycopy = enemy.copy()
                            if not simulateattacktillonedead(playercopy, enemycopy):
                                if cost > highestcost:
                                    highestcost = cost
                else:
                    if i == 1:
                        for ring in ringshop:
                            playercopy = player.copy()
                            playercopy[1] += ring[2]
                            playercopy[2] += ring[3]
                            playercopy[1] += weapon[2]
                            cost = ring[1] + weapon[1]
                            enemycopy = enemy.copy()
                            if not simulateattacktillonedead(playercopy, enemycopy):
                                if cost > highestcost:
                                    highestcost = cost
                    elif i == 2:
                        for ring in ringshop:
                            ringshopcopy = ringshop.copy()
                            tocastintothefire = ring
                            ringshopcopy.remove(tocastintothefire)
                            for ring2 in ringshopcopy: 
                                playercopy = player.copy()
                                playercopy[1] += ring[2]
                                playercopy[2] += ring[3]
                                playercopy[1] += ring2[2]
                                playercopy[2] += ring2[3]
                                playercopy[1] += weapon[2]
                                cost = ring[1] + ring2[1] + weapon[1]
                                enemycopy = enemy.copy()
                                if not simulateattacktillonedead(playercopy, enemycopy):
                                    if cost > highestcost:
                                        highestcost = cost
                    else:
                        playercopy = player.copy()
                        playercopy[1] += weapon[2]
                        cost = weapon[1]
                        enemycopy = enemy.copy()
                        if not simulateattacktillonedead(playercopy, enemycopy):
                            if cost > highestcost:
                                highestcost = cost

    print(highestcost)

part1()
part2()