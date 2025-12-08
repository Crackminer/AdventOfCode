puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2025/day8/day8.txt', 'r') as file:
    puzzleinput = file.read()

import math

testinput = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

def euclideanDistance(coordinate1, coordinate2):
    return math.sqrt(pow((coordinate1[0] - coordinate2[0]), 2)+pow((coordinate1[1]-coordinate2[1]), 2)+pow((coordinate1[2]-coordinate2[2]), 2))

def meanFunc():
    #puzzleinput = testinput
    nums = []
    for line in puzzleinput.splitlines():
        nums.append([int(x) for x in line.split(',')])

    circuits = []

    loops = 0

    prev_dist = -1

    res1 = 0
    res2 = 0

    
    nnum1, nnum2 = None, None

    while True:
        lowestDist = 999999
        nnum1, nnum2 = None, None
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                dist = euclideanDistance(num1, num2)
                if dist == 0:
                    continue
                if dist < lowestDist and dist > prev_dist:
                    lowestDist = dist
                    nnum1 = num1 
                    nnum2 = num2

        
        num1In = False
        num2In = False
        num1index = -1
        num2index = -1

        for k, circuit in enumerate(circuits):
            if nnum1 in circuit:
                num1In = True
                num1index = k
            if nnum2 in circuit:
                num2In  = True
                num2index = k
        if num2index == num1index and (num1index != -1 or num2index != -1):
            loops += 1
            if loops == 1000:
                first, second, third = 1, 1, 1

                for circuit in circuits:
                    if len(circuit) >= first:
                        third, second, first = second, first, len(circuit)
                    
                    elif len(circuit) >= second:
                        third, second = second, len(circuit)
                    
                    elif len(circuit) >= third:
                        third = len(circuit)

                res1 = third * second * first
            prev_dist = lowestDist
            continue
        if num1In:
            if num2In:
                for circuit in circuits[num2index]:
                    if circuit not in circuits[num1index]:
                        circuits[num1index].append(circuit)
                circuits.remove(circuits[num2index])
            else:
                circuits[num1index].append(nnum2)
        elif num2In:
            if num1In:
                for circuit in circuits[num1index]:
                    if circuit not in circuits[num2index]:
                        circuits[num2index].append(circuit)
                circuits.remove(circuits[num1index])
            else:
                circuits[num2index].append(nnum1)
        else:
            circuits.append([nnum1, nnum2])
        loops += 1
        if loops == 1000:
            first, second, third = 1, 1, 1

            for circuit in circuits:
                if len(circuit) >= first:
                    third, second, first = second, first, len(circuit)
                
                elif len(circuit) >= second:
                    third, second = second, len(circuit)
                
                elif len(circuit) >= third:
                    third = len(circuit)

            res1 = third * second * first
        prev_dist = lowestDist
        if len(circuits[0]) == len(nums):
            break


    res2 = nnum1[0] * nnum2[0]

    return res1, res2

p1, p2 = meanFunc()

def part1():
    print(p1)

def part2():
    print(p2)

part1()
part2()